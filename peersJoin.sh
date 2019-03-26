#!/bin/sh
echo "Peers and DataBase"
read numPeersAndDataBase

export CHANNEL_NAME=mychannel

CORE_PEER_LOCALMSPID="Org2MSP"
CORE_PEER_TLS_ROOTCERT_FILE=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt
CORE_PEER_MSPCONFIGPATH=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp
for i in $(seq 0 $numPeersAndDataBase)
do
  CORE_PEER_ADDRESS=peer$i.org2.example.com:7051
  echo $CORE_PEER_ADDRESS
  peer channel join -b mychannel.block
done
