import flet as ft 
from interface import initApp, showPrincipal
import constants
from initialization import init_db
from Modules.customControls import CustomAppBar, CustomUserIcon, CustomSidebar, CustomCardInfo, CustomDatePicker, CustomFilledButton, CustomAnimatedContainer, CustomAutoComplete, CustomNumberField, CustomTooltip, CustomTextField, CustomDropdown, CustomItemsSelector, CustomItemCard, CustomImageContainer
from utils.sessionManager import getCurrentUser, setUser
from config import getDB
from DataBase.crud.user import getUsers
from DataBase.crud.product import getProductByName, getProducts
from utils.imageManager import ImageManager
import time
import asyncio

def main(page: ft.Page):
  page.title = "Kariña System"
  page.theme = ft.Theme(
    scrollbar_theme=ft.ScrollbarTheme(
      track_color={
        ft.MaterialState.DEFAULT: constants.BLACK_GRAY,
      },
      thumb_color={
        ft.MaterialState.DEFAULT: constants.BLACK_GRAY,
      }
    )
  )
  
  page.theme_mode = ft.ThemeMode.LIGHT
  page.bgcolor = constants.WHITE
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.padding = 0 
  
  init_db() 

  setUser("Alfa06N")
  showPrincipal(page)
  # initApp(page)
  
  # from Modules.Sections.SalesSection.components import SaleRecord
  # from DataBase.crud.sale import getSales, getSaleById
  
  # with getDB() as db:
  #   sale = getSaleById(db, 3)
    
  #   saleRecord = SaleRecord(
  #     page=page,
  #     idSale=sale.idSale
  #   )
    
  #   for register in sale.products:
  #     print(register.product.name)
    
  #   page.add(ft.Container(
  #     height=500,
  #     width=600,
  #     content=saleRecord,
  #     alignment=ft.alignment.center,
  #   ))
  

if __name__ == "__main__":
  
  ft.app(target=main)