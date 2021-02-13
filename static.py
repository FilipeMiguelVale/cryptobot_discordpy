#### Paths
fonts_path='Fonts/'
verdana=fonts_path+"verdana.ttf"
verdana_bold=fonts_path+"Verdana_Bold.ttf"
# temporary files
cards_path="cards/"
temp_path="cards/temp/"
logs_path="Logs/"

#### Values
# default number of cards per pack
base_nmr_cards=3
# cards new size for caderneta
resized_size=(480, 672)
# caderneta size
page_columns=6
page_rows=6
# card pack price
pack_price=30
# cards per row in show_cards
show_cards_per_row=6
# default gift points
gift_points = 5
#card_types
card_rarity = ["common","rare","epic","legendary"]

#### Colors
color_success=0x00d62e
color_warning=0xd6c93c
color_problem=0xd60000
color_BTC=0xfcb103
color_eth=0x5a15ed
color_epic=0x7000a3
color_legendary=0x35d482

#### Messages
# Success title
title_success="Success!"
# Warning title
title_warning="Warning!"
# Problem title
title_problem="Something went wrong..."
title_currencies="Your top currencies"
title_btc_price="BTC is at "
title_eth_price="ETH is at "

#### IDs
# Channels
ranking_channel_id = 769632015648555030

### Currencies
currencies=["BTC","GRT","ETH","LTC","LINK","XLM","AAVE","MKR","ALGO","NU","DNT","OXT","CVC"]

def get_url(currencie):
    print(currencie)
    if currencie == "BTC":
        return "https://dynamic-assets.coinbase.com/e785e0181f1a23a30d9476038d9be91e9f6c63959b538eabbc51a1abc8898940383291eede695c3b8dfaa1829a9b57f5a2d0a16b0523580346c6b8fab67af14b/asset_icons/b57ac673f06a4b0338a596817eb0a50ce16e2059f327dc117744449a47915cb2.png"
    if currencie == "GRT":
        return "https://www.marketbeat.com/logos/cryptocurrencies/6719.png"
    if currencie == "ETH":
        return "https://res-2.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1476103033/xfu7exy5y6rkscsm1kns.png"
    if currencie == "LTC":
        return "https://smartbettingguide.com/app/uploads/2020/02/litecoin-22.png"
    if currencie == "LINK":
        return "https://dynamic-assets.coinbase.com/9e34c547e363744ad9e5d140d098f498ee8959a2c175366765beb000c24695712697b3aa8d972e75e4d6c79a5c16e496a78fe30094638b1ad5fea45db71c82df/asset_icons/351b8b5f92576806a20692c98ae00c4d930117e44b26f217ab2bef5b29b3e312.png"
    if currencie == "XLM":
        return "https://dynamic-assets.coinbase.com/ddaf9d27a2388105c5568c68ebe4078d057efac1cb9b091af6a57f4d187cf06b2701b95f75bd148d3872df32b69ebb678de71a42da317370aaec7d6448bda379/asset_icons/80782fe2d690f299e7f5bb9b89af87e1db75769e59c14fa0257054c962401805.png"
    if currencie == "AAVE":
        return "https://dynamic-assets.coinbase.com/6ad513d3c9108b163cf0a4c9fd3441cadcb9cf656ea7b9fb333eb7e4a94cd503528e0a94188285d31aedfc392f0793fd4161f7ad4e04d5f6b82e4d70a314d295/asset_icons/80f3d2256652f5ccd680fc48702d130dd01f1bd7c9737fac560a02949efac3b9.png"
    if currencie == "MKR":
        return "https://isthiscoinascam.com/logo/m/maker-128xa6ce9b15249ee215ea3e272ca9a275d2.png"
    if currencie == "ALGO":
        return "https://dynamic-assets.coinbase.com/434cf9473be68c296f9c213b64a8caaebeb0f0fcf4096f38af3175eead7107425676652c9219c003f2acaafdcb07bce1f4862fe4f3f692ca1ae1da3c3dbff546/asset_icons/40447ba4170da28e92cf5c02d5675103d44d75fd6076ad8b0f5a953b3d4d3b9e.png"
    if currencie == "NU":
        return "https://dynamic-assets.coinbase.com/462fb777ebe2252a550afc2b60bfe8e2722d913f00c2f5c307bce173f0a2587fd6d185bf8ba349e133b150305373fcd4a516ce7566ee312c718595d73a585f22/asset_icons/8c183b0f4f9865818c59bb1e7070176eb1088f2d8ec3e868494a61450946395a.png"
    if currencie == "DNT":
        return "https://dynamic-assets.coinbase.com/577411f8690b794940a3b2c1d41bd3e5abfb7cccbb0841b7f38be34738ddaa2e1dde03ca463ff4b495f1fa46807364347032db065a1606427e26dc56ddda927b/asset_icons/ee9de82c22e44db793002d1ce558e62523f63d847f5d0ddf49da18cd338da946.png"
    if currencie == "OXT":
        return "https://dynamic-assets.coinbase.com/22b24ad9886150535671f158ccb0dd9d12089803728551c998e17e0f503484e9c38f3e8735354b5e622753684f040488b08d55b8ef5fef51592680f0c572bdfe/asset_icons/023010d790b9b1f47bc285802eafeab3d83c4de2029fe808d59935fbc54cdd7c.png"
    if currencie == "CVC":
        return "https://dynamic-assets.coinbase.com/4b2384d50867dc6984a4fd96e62548f1a1a86c9bb4f90ed93b2a8795238c53f7c67768ddda5860a24fdfbf4e041b8fe16d32fdc2e893da131024c57f019821e3/asset_icons/748af2ecb578424b712a0498ec4653bd336db3d462479496f376e5e958df08db.png"



