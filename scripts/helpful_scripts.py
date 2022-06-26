# Here we put our common code which we have to use ofter so that we can directly use them in deploy file to make code look more clean

from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork-dev","mainnet-fork"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")

    # If we already deployed MockV3Aggregator then whats the point of deploying it again n again
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS,
            STARTING_PRICE,
            {
                "from": get_account()
            },  # toWei function automatically put 18 zeros after 2000
        )
    print("Mock Deployed!!!")
