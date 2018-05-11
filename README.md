# pacli
-- This is a Work In Progress updated version of the original pacli client available at https://github.com/PeerAssets/pacli --

Simple CLI PeerAssets client. 

Implemented using `pypeerassets` Python library, this command line program is useful as companion utility during PeerAssets development and testing.
It is built for headless (CLI) usage via intuitive and easy to learn set of commands.
All deck id's are shortened by taking only 20 first characters of full sha256 deck id, this is to allow easier user interaction
and use less screen space. You can always get full deck id by calling `pacli deck --info` command as shown bellow.
When querying for deck you can use short deck id, full deck id and deck name.
Using short or full deck id is advised as decks can have a same name.


accepted commands at the moment:

```ipython __main__.py deck <function> <argument 1> <argument 2>```

Example:

```ipython __main__.py deck find willyB True```

returns:

```
+Deck id: 17d24b9bca5a090a24af138c2e085f80621396e8c7b6f820dee7140aee15cac1 ------------+
| asset name | issuer                             | issue mode | decimals | issue time |
+------------+------------------------------------+------------+----------+------------+
| willyB     | n1ga7fPBerBZDK9NPru39Fanzj9cPhbumM | 4          | 2        | 1525317673 |
+------------+------------------------------------+------------+----------+------------+
+('willyB cards',)-------------------+----------------------------------------+--------+-----------+------------+
| sender                             | receiver                               | amount | type      | timestamp  |
+------------------------------------+----------------------------------------+--------+-----------+------------+
| n1ga7fPBerBZDK9NPru39Fanzj9cPhbumM | ['n4SqkasjPMKWbfgkuEJHSdK8B22GXfKpju'] | [5]    | CardIssue | 0          |
| n1ga7fPBerBZDK9NPru39Fanzj9cPhbumM | ['n4SqkasjPMKWbfgkuEJHSdK8B22GXfKpju'] | [1]    | CardIssue | 1525818864 |
| n1ga7fPBerBZDK9NPru39Fanzj9cPhbumM | ['n4SqkasjPMKWbfgkuEJHSdK8B22GXfKpju'] | [5]    | CardIssue | 1525837744 |
| n1ga7fPBerBZDK9NPru39Fanzj9cPhbumM | ['n4SqkasjPMKWbfgkuEJHSdK8B22GXfKpju'] | [10]   | CardIssue | 1525839709 |
+------------------------------------+----------------------------------------+--------+-----------+------------+

```

Based on the decks with the name "willyB" and cards = True, returning all Card Transfers associated with it.