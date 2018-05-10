import fire
import pypeerassets as pa
from pacli.provider import provider
from pacli.config import Settings
from terminaltables import AsciiTable
from utils import print_table

class Deck:

    @classmethod
    def list(self):
        decks = list(pa.find_all_valid_decks(provider, Settings.deck_version,
                                             Settings.production))

    @classmethod
    def deck_title(self, deck):
        return "Deck id: " + deck.id + " "

    @classmethod
    def find(self, key, card: bool=False):
        '''
        Find specific deck by key, with key being:
        <id>, <name>, <issuer>, <issue_mode>, <number_of_decimals>
        '''

        #Gather all decks from the node
        decks = pa.find_all_valid_decks(provider,
                                        Settings.deck_version,
                                        Settings.production)

        #Iterate through the list of Deck dicts
        for d in decks: 
            if key in d.__dict__.values():
                #Print deck information as an ASCII table
                print_table(
                    title=Deck.deck_title(d),
                    heading=("asset name", "issuer", "issue mode", "decimals", "issue time"),
                    data=[[ #Use getattr() to cherrypick key values from dict
                        getattr(d, attr) for attr in 
                        ["name", "issuer", "issue_mode", "number_of_decimals", "issue_time"] ]])

    @classmethod
    def new(self, name: str, number_of_decimals: int, issue_mode: int,
            asset_specific_data: bytes=None):

        network = Settings.network
        production = Settings.production
        version = Settings.version

        new_deck = pa.Deck(name, number_of_decimals, issue_mode, network,
                           production, version, asset_specific_data)

        pa.deck_spawn(provider, Settings.key, new_deck, Settings.change)

class Card:

    @classmethod
    def find(self, deck)
        ''' Find all associated cards '''
        cards = pa.find_card_transfers(provider, deck)
        return cards

def main():

    fire.Fire({
        'deck': Deck()
        })


if __name__ == '__main__':
    main()