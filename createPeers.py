#!/usr/bin/env python
# -*- coding: utf-8 -*-

arq = open('./docker-composer-new-peer.yaml','w')
count = int(raw_input('Peers and DataBase: '))
numPeer = 2
portPeer = 11
numCouchdb = 4
portCouchdb = 9
text = """# Copyright IBM Corp. All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0
#

version: '2'

networks:
  byfn:

services:
"""

for num in range(count):
    text+="""
  couchdb"""+str(numCouchdb)+""":
    container_name: couchdb"""+str(numCouchdb)+"""        
    image: hyperledger/fabric-couchdb
    # Populate the COUCHDB_USER and COUCHDB_PASSWORD to set an admin user and password
    # for CouchDB.  This will prevent CouchDB from operating in an "Admin Party" mode.
    environment:
    - COUCHDB_USER=
    - COUCHDB_PASSWORD=
    # Comment/Uncomment the port mapping if you want to hide/expose the CouchDB service,
    # for example map it to utilize Fauxton User Interface in dev environments.
    ports:
    - \""""+str(portCouchdb)+"""984:5984"
    networks:
    - byfn

  peer"""+str(numPeer)+""".org2.example.com:
    container_name: peer"""+str(numPeer)+""".org2.example.com
    extends:
      file: base/peer-base.yaml
      service: peer-base
    environment:
    - CORE_LEDGER_STATE_STATEDATABASE=CouchDB
    - CORE_LEDGER_STATE_COUCHDBCONFIG_COUCHDBADDRESS=couchdb4:5984
    # The CORE_LEDGER_STATE_COUCHDBCONFIG_USERNAME and CORE_LEDGER_STATE_COUCHDBCONFIG_PASSWORD
    # provide the credentials for ledger to connect to CouchDB.  The username and password must
    # match the username and password set for the associated CouchDB.
    - CORE_LEDGER_STATE_COUCHDBCONFIG_USERNAME=
    - CORE_LEDGER_STATE_COUCHDBCONFIG_PASSWORD=
    - CORE_PEER_ID=peer"""+str(numPeer)+""".org2.example.com
    - CORE_PEER_ADDRESS=peer"""+str(numPeer)+""".org2.example.com:7051
    - CORE_PEER_GOSSIP_EXTERNALENDPOINT=peer"""+str(numPeer)+""".org2.example.com:7051
    - CORE_PEER_GOSSIP_BOOTSTRAP=peer1.org2.example.com:7051
    - CORE_PEER_LOCALMSPID=Org2MSP
    volumes:
    - /var/run/:/host/var/run/
    - ./crypto-config/peerOrganizations/org2.example.com/peers/peer"""+str(numPeer)+""".org2.example.com/msp:/etc/hyperledger/fabric/msp
    - ./crypto-config/peerOrganizations/org2.example.com/peers/peer"""+str(numPeer)+""".org2.example.com/tls:/etc/hyperledger/fabric/tls
    ports:
    - """+str(portPeer)+"""051:7051
    - """+str(portPeer)+"""053:7053    
    depends_on:
    - couchdb"""+str(numCouchdb)+"""
    networks:
    - byfn
    
    """
    numPeer = numPeer + 1
    print('\n'+str(numPeer))
    numCouchdb = numCouchdb + 1
    portPeer = portPeer + 1
    portCouchdb = portCouchdb + 1
        
arq.write(text)
arq.close
