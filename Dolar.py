from playwright.sync_api import sync_playwright

def buscar_cotacao_dolar():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)
        pagina = navegador.new_page()
        pagina.goto("https://dolarhoje.com/")

        campo = pagina.wait_for_selector("#nacional")
        valor = campo.input_value()

        navegador.close()
        return valor
