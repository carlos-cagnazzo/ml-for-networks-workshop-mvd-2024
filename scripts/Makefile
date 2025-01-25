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
WINDOW="6"

features_rrc05 : ../data/2005-moscow-blackout-ris-rrc05.csv
	./feature_0.py --input ../data/2005-moscow-blackout-ris-rrc05.csv --window $(WINDOW) --head $(HEAD) --output ../features/2005-moscow-blackout/w10s/feature_0_rrc05.csv
	./feature_1.py --input ../data/2005-moscow-blackout-ris-rrc05.csv --window $(WINDOW) --head $(HEAD) --output ../features/2005-moscow-blackout/w10s/feature_1_rrc05.csv
	./feature_2.py --input ../data/2005-moscow-blackout-ris-rrc05.csv --window $(WINDOW) --head $(HEAD) --output ../features/2005-moscow-blackout/w10s/feature_2_rrc05.csv
	./feature_3.py --input ../data/2005-moscow-blackout-ris-rrc05.csv --window $(WINDOW) --head $(HEAD) --output ../features/2005-moscow-blackout/w10s/feature_3_rrc05.csv
	./feature_4.py --input ../data/2005-moscow-blackout-ris-rrc05.csv --window $(WINDOW) --head $(HEAD) --output ../features/2005-moscow-blackout/w10s/feature_4_rrc05.csv
	./feature_5.py --input ../data/2005-moscow-blackout-ris-rrc05.csv --window $(WINDOW) --head $(HEAD) --output ../features/2005-moscow-blackout/w10s/feature_5_rrc05.csv
