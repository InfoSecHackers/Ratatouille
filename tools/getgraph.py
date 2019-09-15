import re,fileinput,os,sys
import pandas as pd
import json
import re
import warnings
from datetime import date
from geoip import geolite2

def getgraph():

	try:

		path=os.getcwd()+"/pcap_downloads/"
		os.chdir(path)
		osw= os.walk(path)

		for path, dirs, files in os.walk(path):
			for filename in files:

				try:

					csvname = filename.replace('.pcap','.csv')
					fullpath = os.path.join(path, filename)
					fullpath_csv = os.path.join(path, csvname)
					try:

						os.system("tshark -r %s -Y 'ip'  -T fields -E separator=, -E header=y -e frame.number -e ip.src -e ip.dst  > %s" %(fullpath,fullpath_csv))
					except Exception as te:
						print (te)
						exit(0)
					warnings.filterwarnings('ignore')

					pcap_data = pd.read_csv(fullpath_csv, index_col='frame.number')
					dataframe = pcap_data
					src_dst = dataframe[["ip.src","ip.dst"]]

					def ip_matcher(address):
					# Used to validate if string is an ipaddress
						ip = re.match(
						'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', address)
						if ip:
							return True
						else:
							return False
					src_dst.rename(columns={"ip.src":"source","ip.dst":"target"}, inplace=True)
					src_dst['valid_src'] = src_dst.source.apply(ip_matcher)
					src_dst['valid_target'] = src_dst.target.apply(ip_matcher)

					valid_src_dest = src_dst[(src_dst.valid_src==True) & (src_dst.valid_target==True)]
					grouped_src_dst = valid_src_dest.groupby(["source","target"]).size().reset_index()
					unique_ips = pd.Index(grouped_src_dst['source']
					                      .append(grouped_src_dst['target'])
					                      .reset_index(drop=True).unique())

					group_dict = {}
					counter = 0
					for ip in unique_ips:
					    breakout_ip = re.match("^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
					    if breakout_ip:
					        net_id = '.'.join(breakout_ip.group(1,2,3))
					        if net_id not in group_dict:
					            counter += 1
					            group_dict[net_id] = counter
					        else:
					            pass
					grouped_src_dst.rename(columns={0:'count'}, inplace=True)
					temp_links_list = list(grouped_src_dst.apply(lambda row: {"source": row['source'], "target": row['target'], "value": row['count']}, axis=1))
					links_list = []
					for link in temp_links_list:
						try:
						    record = {"value":link['value'], "source":unique_ips.get_loc(link['source']),
						     "target": unique_ips.get_loc(link['target'])}
						    links_list.append(record)
						except Exception as lnx:
							print lnx
							#pass
					nodes_list = []

					for ip in unique_ips:
					    breakout_ip = re.match("^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
					    if breakout_ip:
					        net_id = '.'.join(breakout_ip.group(1,2,3))
					        cn_print = geolite2.lookup(ip)
					        ip = ip+'-'+cn_print.country
					        nodes_list.append({"name":ip, "group": group_dict.get(net_id)})

					json_prep = {"links":links_list, "nodes":nodes_list}

					json_prep.keys()

					json_dump = json.dumps(json_prep, indent=1, sort_keys=True)

					#pd.DataFrame(json_prep['nodes']).head()
					#pd.DataFrame(json_prep['links']).head()

					dirdate= str(date.today())
					fname = os.path.split(os.getcwd())[0]
					filename = csvname.replace('.csv','')
					outfname = fname +"/output/graph/"+ dirdate +"/"+ filename
					print ("outfilename"+outfname)
					outfolder = fname +"/output/graph/"+dirdate
					try:
					    os.mkdir(outfolder)
					    
					except Exception as e:
					    pass
					json_out = open(outfname,'w')
					json_out.write(json_dump)
					json_out.close()

				except Exception as ex:
					print (ex)
					pass

	except Exception as e:

		print (e)
		os.chdir("..")
		getgraph()