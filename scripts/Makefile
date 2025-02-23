## Pipeline para procesar y agreagar los datos

# | bgpreader \-w '2024-01-01 00:00:00','2024-01-01 23:59:59' \-p ris \-c rrc00 \-t updates |
# | :---- |
# 
# * \-w , “time window”, get messages that were received between these date and times  
# * \-p , data source, in this case RIPE RIS  
# * \-c , collector (rrc00 in this case)  
# * \-t , message types, in this case UPDATES
#

HEAD="100000000"
WINDOW="06"

help:
	@echo "Makefile for producing feature csv files from bgpstream data"
	@echo " ---- "
	@echo "Available targets: "
	@echo " "
	@echo "	help: This help message"
	@echo "	moscow_blackout_features_rrc05    : ../data/2005-moscow-blackout-ris-rrc05.csv"
	@echo "	equinix_leak_features_rrc11       : ../data/2017-level3-route-leak-ris-rrc11.csv"
	@echo "	equinix_leak_features_rrc00       : ../data/2017-level3-route-leak-ris-rrc00.csv"
	@echo "	telstra-optus-leak_features_rrc23 : ../data/2023-telstra-optus-route-leak-ris-rrc23.csv"
	@echo "	rostelecom-leak_features_rrc05    : ../data/2020-rostelecom-leak-ris-rrc05.csv "


moscow_blackout_features_rrc05 : ../data/2005-moscow-blackout-ris-rrc05.csv
	./feature_0.py --input ../data/2005-moscow-blackout-ris-rrc05.csv --window $(WINDOW) --head $(HEAD) --output ../features/2005-moscow-blackout/w06s/feature_0_rrc05.csv
	./feature_1.py --input ../data/2005-moscow-blackout-ris-rrc05.csv --window $(WINDOW) --head $(HEAD) --output ../features/2005-moscow-blackout/w06s/feature_1_rrc05.csv
	./feature_2.py --input ../data/2005-moscow-blackout-ris-rrc05.csv --window $(WINDOW) --head $(HEAD) --output ../features/2005-moscow-blackout/w06s/feature_2_rrc05.csv
	./feature_3.py --input ../data/2005-moscow-blackout-ris-rrc05.csv --window $(WINDOW) --head $(HEAD) --output ../features/2005-moscow-blackout/w06s/feature_3_rrc05.csv
	./feature_4.py --input ../data/2005-moscow-blackout-ris-rrc05.csv --window $(WINDOW) --head $(HEAD) --output ../features/2005-moscow-blackout/w06s/feature_4_rrc05.csv
	./feature_5.py --input ../data/2005-moscow-blackout-ris-rrc05.csv --window $(WINDOW) --head $(HEAD) --output ../features/2005-moscow-blackout/w06s/feature_5_rrc05.csv

## 2017 Level3 Route Leak

equinix_leak_features_rrc11 : INPUT      = "../data/2017-level3-route-leak-ris-rrc11.csv"
equinix_leak_features_rrc11 : OUTPUT_DIR = "../features/2017-level3-leak/w$(WINDOW)s/"
equinix_leak_features_rrc11 : HEAD       = "1000000000"
equinix_leak_features_rrc11 : WINDOW     = "06"

equinix_leak_features_rrc11 : ../data/2017-level3-route-leak-ris-rrc11.csv
	mkdir -p $(OUTPUT_DIR)
	./feature_0.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_0_rrc11.csv 
	./feature_1.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_1_rrc11.csv 
	./feature_2.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_2_rrc11.csv 
	./feature_3.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_3_rrc11.csv 
	./feature_4.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_4_rrc11.csv 
	./feature_5.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_5_rrc11.csv 


equinix_leak_features_rrc00 : INPUT      = "../data/2017-level3-route-leak-ris-rrc00.csv"
equinix_leak_features_rrc00 : OUTPUT_DIR = "../features/2017-level3-leak/w$(WINDOW)s/"
equinix_leak_features_rrc00 : HEAD       = "1000000000"
equinix_leak_features_rrc00 : WINDOW     = "06"


equinix_leak_features_rrc00 : ../data/2017-level3-route-leak-ris-rrc00.csv
	mkdir -p $(OUTPUT_DIR)
	./feature_0.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_0_rrc00.csv 
	./feature_1.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_1_rrc00.csv 
	./feature_2.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_2_rrc00.csv 
	./feature_3.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_3_rrc00.csv 
	./feature_4.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_4_rrc00.csv 
	./feature_5.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_5_rrc00.csv 


# -----------------------------------------------------------------------------------------------------------------------
# 2023 TELSTRA OPTUS ROUTE LEAK
# -----------------------------------------------------------------------------------------------------------------------
telstra-optus-leak_features_rrc23 : INPUT      = "../data/2023-telstra-optus-route-leak-ris-rrc23.csv"
telstra-optus-leak_features_rrc23 : OUTPUT_DIR = "../features/2023-telstra-optus-leak/w$(WINDOW)s/"
telstra-optus-leak_features_rrc23 : HEAD       = "50000000"
telstra-optus-leak_features_rrc23 : WINDOW     = "06"


telstra-optus-leak_features_rrc23 : ../data/2023-telstra-optus-route-leak-ris-rrc23.csv
	mkdir -p $(OUTPUT_DIR)
	./feature_0.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_0_rrc23.csv 
	./feature_1.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_1_rrc23.csv 
	./feature_2.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_2_rrc23.csv 
	./feature_3.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_3_rrc23.csv 
	./feature_4.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_4_rrc23.csv 
	./feature_5.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_5_rrc23.csv 

# -----------------------------------------------------------------------------------------------------------------------
# 2020 ROSTELECOM LEAK
# -----------------------------------------------------------------------------------------------------------------------
rostelecom-leak_features_rrc05 : INPUT      = "../data/2020-rostelecom-leak-ris-rrc05.csv"
rostelecom-leak_features_rrc05 : OUTPUT_DIR = "../features/2020-rostelecom-leak/w$(WINDOW)s/"
rostelecom-leak_features_rrc05 : HEAD       = "50000000"
rostelecom-leak_features_rrc05 : WINDOW     = "06"


rostelecom-leak_features_rrc05 : ../data/2020-rostelecom-leak-ris-rrc05.csv
	mkdir -p $(OUTPUT_DIR)
	./feature_0.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_0_rrc05.csv 
	./feature_1.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_1_rrc05.csv 
	./feature_2.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_2_rrc05.csv 
	./feature_3.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_3_rrc05.csv 
	./feature_4.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_4_rrc05.csv 
	./feature_5.py --input $(INPUT) --window $(WINDOW) --head $(HEAD) --output $(OUTPUT_DIR)/feature_5_rrc05.csv 
