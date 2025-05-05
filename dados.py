# Link do site / Website link
swaglabs = "https://www.saucedemo.com/"

# Login do usuário / User login
usuario = ('//*[@id="user-name"]', "performance_glitch_user")
senha = ('//*[@id="password"]', "secret_sauce")

# Produtos a serem adicionados no carrinho / Products to be added to the cart
produtos = [
    '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]',
    '//*[@id="add-to-cart-sauce-labs-backpack"]'
]

# Carrinho / Cart
checkout = (
    '//*[@id="shopping_cart_container"]/a',
    '//*[@id="checkout"]'
)

# Caminho dos dados do cliente / Xpaths for customer data fields
caminhos_dados = (
    '//*[@id="first-name"]',
    '//*[@id="last-name"]',
    '//*[@id="postal-code"]'
)

# Dados do cliente / Customer data
campo_dados = (
    "Patrícia",
    "Regina",
    "95500000"
)

# Finalizando compra / Finalizing purchase
botoes_final = (
    '//*[@id="continue"]',
    '//*[@id="finish"]'
)