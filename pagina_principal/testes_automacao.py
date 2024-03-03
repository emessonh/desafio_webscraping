from django.shortcuts import render, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib import messages
import time
from selenium.webdriver.support.ui import WebDriverWait
import requests
import os
from playwright.sync_api import sync_playwright
import time


driver = webdriver.Chrome()
try:
    driver.get('http://www.infraestrutura.mg.gov.br/images/documentos/precosetop/2023/Planilha-Precos-SETOP-2023/08-Agosto/sem-desoneracao/202308_Planilha_Precos_SETOP_Central_SEM_DESONERACAO.xlsx')
    time.sleep(10)
    driver.close()
    print('funcionou')
except Exception:
    driver.close()
    print('não funcionou')

