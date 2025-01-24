import flet as ft 
from interface import initApp, showPrincipal
import constants
from initialization import init_db
from Modules.customControls import CustomAppBar, CustomUserIcon, CustomSidebar, CustomCardInfo, CustomDatePicker, CustomFilledButton, CustomAnimatedContainer, CustomAutoComplete, CustomNumberField, CustomTooltip, CustomTextField, CustomDropdown, CustomItemsSelector, CustomItemCard, CustomImageContainer
from utils.sessionManager import getCurrentUser, setUser
from config import getDB
from DataBase.crud.user import getUsers, getUserByUsername, updateUser
from DataBase.crud.product import getProductByName, getProducts
from DataBase.crud.category import getCategories, removeCategory
from utils.imageManager import ImageManager
import time
import asyncio
from DataBase.crud.transaction import getTransactions

def main(page: ft.Page):
  page.title = "Kariña System"
  page.theme = ft.Theme(
    scrollbar_theme=ft.ScrollbarTheme(
      track_color={
        ft.ControlState.DEFAULT: constants.BLACK_GRAY,
      },
      thumb_color={
        ft.ControlState.DEFAULT: constants.BLACK_GRAY,
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

 
if __name__ == "__main__":
  
  ft.app(target=main)