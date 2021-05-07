import yaml
from mcl import MCL

def load_config():
	return yaml.load(open("config.yaml", 'r'), yaml.Loader)

if __name__=="__main__":
	main_control_loop = MCL({"read": load_config(), "actuate": ["Downlink_Producer"]})
	print("EXECUTING MAIN CONTROL LOOP...")
	main_control_loop.execute()

