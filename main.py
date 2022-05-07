# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:29:57 2022
@author: zaytoun (https://github.com/zaytoun/scihub.py)
@author: Israel Dryer (https://github.com/israel-dryer/ttkbootstrap)
@author: Chris Sun finished GUI part based on the work that has done by zaytoun and Israel Dryer
"""

#**********************PROGRAM PART***********************
# Import scihub 
from scihub import SciHub

#************************GUI PART*************************
# Import modules
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.constants import *
from tkinter.filedialog import askdirectory,askopenfilename

class SciHubDownloader(ttk.Frame):
    def __init__(self,master):
        super().__init__(master,padding=(20,10))
        self.pack(fill=BOTH,expand=YES)

        # Set path
        self.path = ''

        # Form logo
        self.search_image = tk.PhotoImage(file='searchlogo.png')
        self.search_information = tk.Label(self,image=self.search_image,width=600,height=180)
        self.search_information.pack(fill=X,pady=10)
        
        # Form header
        self.header = 'PLEASE ENTER ARTICLE TITLE OR URL OR DOI:'
        self.hdr = ttk.Label(master=self,text=self.header,bootstyle=DARK,width=80,font='-size 12 -weight bold')
        self.hdr.pack(fill=X,pady=10)
        
        # Form entry
        self.entry = ttk.Entry(self,font='-size 12 -weight bold')
        self.entry.pack(fill=BOTH,expand=YES)
        
        # Form button
        # Download button
        self.dnl_btn = ttk.Button(self,
                                  text='DOWNLOAD',
                                  command=self.download,
                                  bootstyle=SUCCESS,
                                  )
        self.dnl_btn.pack(side=RIGHT,pady=10)
        
        # Clear button
        self.clr_btn = ttk.Button(self,
                                  text='CLEAR INPUT',
                                  command=self.clear,
                                  bootstyle=DANGER)
        self.clr_btn.pack(side=RIGHT,pady=10,padx=5)

        # Save path button
        self.brs_btn = ttk.Button(self,
                                  text='SAVE PATH',
                                  command=self.save,
                                  bootstyle=INFO)
        self.brs_btn.pack(side=LEFT,pady=10)
        
    # Download button function
    def download(self):
        for term in self.entry.get().split(';'):
            if term[0:4] == 'http' or term[0:3] == '10.':
                sh = SciHub()
                if len(self.path) != 0:
                    sh.download(term, self.path)
                else:
                    sh.download(term)
                print('OK:', Messagebox.show_info(
                    message='Finish downloading!',
                    title='DOWNLOAD PROCESS',
                ))
            else:
                artName = term
                request = artName
                downUrl = self.search_article(request)
                if downUrl == '':
                    print('retrycancel:', Messagebox.show_error(
                        message='Cannot find the related article, please search again!',
                        title='SEARCH ERROR',
                    ))
                else:
                    pdf = self.download_article(downUrl)
                    with open(self.path+'%s.pdf' % request, 'wb') as f:
                        f.write(pdf)
                    print('OK:', Messagebox.show_info(
                        message='Finish downloading!',
                        title='DOWNLOAD PROCESS',
                    ))

    # Clear button function
    def clear(self):
        self.entry.delete(0,END)
        
    # Save button function
    def save(self):
        self.path = askdirectory()+'/'
        self.path = self.path.replace('/','\\')
        self.path = self.path.replace('\\','\\\\')
        #print(self.path)

    def search_article(self,artName):
        sh = SciHub()
        url = sh._get_available_scihub_urls()[4]
        #url = 'https://sci-hub.st'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Content-Length': '123',
                   'Origin': url,  # scihub source
                   'Connection': 'keep-alive',
                   'Upgrade-Insecure-Requests': '1'}
        data = {'sci-hub-plugin-check': '', 'request': artName}
        res = requests.post(url, headers=headers, data=data)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        iframe = soup.find(id='pdf')
        if iframe == None:
            return ''
        else:
            downUrl = iframe['src']
            if 'http' not in downUrl:
                downUrl = 'https:' + downUrl
            return downUrl

    def download_article(self,downUrl):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Accept-Encoding':'gzip, deflate, br',
               'Connection':'keep-alive',
               'Upgrade-Insecure-Requests':'1'}
        res = requests.get(downUrl,headers = headers)
        return res.content

if __name__ == '__main__':
    app = ttk.Window('SCI-HUB DOWNLOADER Ver.2.0    -GUI by ChrisSun-','minty')
    SciHubDownloader(app)
    app.mainloop()