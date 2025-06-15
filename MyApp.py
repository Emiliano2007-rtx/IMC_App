import flet as ft 

def Main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title="IMC Calculadora"
    page.bgcolor = "#FFFFFF"
    page.add(ft.Text("Calculadora de IMC",weight="bold",size=35, color="#0EAF29"))
    page.add(ft.Divider())
    page.add(ft.Text("Calcula tu IMC",weight="bold",size=25, color="#7F8C8D"))
    page.add(ft.Text("",weight="bold",size=35, color="#7F8C8D"))

    txt_alt = ft.TextField(label="Ingresa tu altura (Metros)",
                           text_style=ft.TextStyle(size=15,color="#7F8C8D",weight="bold"),
                           text_align=ft.TextAlign.CENTER,
                           label_style=ft.TextStyle(size=15,color="#1187cc",weight="bold"),
                           border=1,border_color="#50E3E2",border_radius=10)
    
    txt_peso = ft.TextField(label="Ingresa tu peso (Kg)",
                            text_style=ft.TextStyle(size=15,color="#7F8C8B",weight="bold"),
                            text_align=ft.TextAlign.CENTER,
                            label_style=ft.TextStyle(size=15,color="#1187cc",weight="bold"),
                            border=1,border_color="#50E3E2",border_radius=10)
    
    
    imcText=ft.Text(color="#0EAF29",weight="bold",size=15)
    imcR=ft.Text(color="#2E3C50",weight="bold",size=15)
    pesoimc=ft.Text(color="#EE730E",weight="bold",size=15)
    divisor=ft.Divider()
    Dev=ft.Text("Made by: Emiliano Alvarado.Dev",color="#868686",weight="bold",size=15)
    
    
    def Calc(e):

     try:  
        Altura=txt_alt.value
        Peso=txt_peso.value
        imc=float(Peso)/float(Altura)**2
        imcText.value=f"IMC"
        imcR.value = round(imc,2)

   
        
        if imc<=18.5:
           pesoimc.value=f"Peso bajo"
        
        elif imc >= 30:
           pesoimc.value=f"Obesidad"

        elif imc >= 25:
           pesoimc.value=f"Sobrepeso"

        else:
           pesoimc.value=f"Peso normal"

        page.update()

     except:   
        imcR.value=f"Error: Ingrese un valor valido"
        page.update()

        
    btn = ft.ElevatedButton("Calcular",
                            bgcolor="#50E3E2",
                            color="white",
                            width=200,
                            height=50,
                            style=ft.ButtonStyle(
                               text_style=ft.TextStyle(
                                  size=20,
                                  weight="bold"
                               )
                            ),
                            on_click=(Calc))
  
    page.add(txt_alt,txt_peso,btn,divisor, imcText,imcR,pesoimc,divisor,Dev)

ft.app(target=Main,view=ft.WEB_BROWSER, port=8000)    