from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from itertools import zip_longest
import random
import string

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


class ADFGVX:

    def encode(self,message,keyword,alphabet):
        MAGIC = 'ADFGVX'
        # remove duplicate character from keyword -> key
        # keyword = 'checkio' -> key = ['c','h','e','k','i','o']

        print (alphabet)
        key = []
        for c in keyword:
            if c not in key: key.append (c)

        # make sort index -> k
        # keyword = 'cipher' -> k = [0, 4, 3, 2, 1, 2, 5]
        n = len (key)
        k = sorted (range (n),key=lambda i:key[i])

        # encode
        # message = 'I am going' ->
        # s = ['F','A','D','V','A','G','X','X','D','X','F','A','G','D','X','X']
        s = []
        for c in message.lower ():
            if c.isalpha () or c.isdigit ():
                row,col = divmod (alphabet.index (c),6)
                s += [MAGIC[row],MAGIC[col]]

        # reorder
        # reorder index = [0, 6, 12, 4, 10, 3, 9, 15, 1, 7, 13, 2, 8, 14, 5, 11]
        return ''.join (s[j] for i in k for j in range (i,len (s),n))

    def decode(self,message,keyword,alphabet):
        MAGIC = 'ADFGVX'

        # remove duplicate character from keyword -> key
        # keyword = 'checkio' -> key = ['c', 'h', 'e', 'k', 'i', 'o']
        secret_alphabet1 = "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g"

        key = []
        for c in keyword:
            if c not in key: key.append (c)

        # make sort index -> k
        # keyword = 'cipher' -> k = [0, 4, 3, 2, 1, 2, 5]
        n = len (key)
        k = sorted (range (n),key=lambda i:key[i])

        # make reorder index
        # len(message) == 16 ->
        # x = [0, 6, 12, 4, 10, 3, 9, 15, 1, 7, 13, 2, 8, 14, 5, 11]
        m = len (message)
        x = [j for i in k for j in range (i,m,n)]

        # reorder
        # message = 'FXGAFVXXAXDDDXGA' ->
        # y = ['F','A','D','V','A','G','X','X','D','X','F','A','G','D','X','X']
        y = [''] * m
        for i,c in zip (x,message): y[i] = c

        # decode
        # y -> s = ['i','a','m','g','o','i','n','g']
        s = []
        for i in range (0,m,2):
            row,col = y[i:i + 2]
            s.append (alphabet[6 * MAGIC.index (row) + MAGIC.index (col)])
        return ''.join (s)


class ADFGX:


    def encode(self,plaintext,key,square):
        ADFGX = 'A','D','F','G','X'
        ciphertext = ''
        if combobox2.get () == "EN":
            exception,ij = ('i','j') if 'j' in square else ('j','i')
        elif combobox2.get () == "CZ":
            exception,ij = ('q','k') if 'q' in square else ('q','k')


        for char in plaintext:
            index = square.index (char) if char != exception else square.index (ij)
            y,x = divmod (index,5)
            ciphertext += ADFGX[y] + ADFGX[x]
        columns = len (key)
        keymatrix = [ch + ciphertext[i::columns] for i,ch in enumerate (key)]
        keymatrix.sort ()
        return ' '.join (column[1:] for column in keymatrix)

    def decode(self,ciphertext,key,square):
        ADFGX = 'A','D','F','G','X'
        eky = sorted (key)
        columns = ciphertext.split ()
        keymatrix = [columns[eky.index (ch)] for ch in key]
        ciphertext = ''.join (''.join (row) for row in zip_longest (*keymatrix,fillvalue=''))
        plaintext = ''
        for j,i in zip (*[iter (ciphertext)] * 2):
            plaintext += square[ADFGX.index (j) * 5 + ADFGX.index (i)]
        return plaintext





def type_change(event):
    if combobox1.get () == "5x5":
        combobox2.grid (row=0,column=2,sticky="w",pady=5,padx=10,columnspan=2)
        table_text.set ("")
        before_entry.configure (state='normal')
    elif combobox1.get () == "6x6":
        combobox2.grid_forget ()
        table_text.set ("")
        before_entry.configure (state='normal')


def type_change1(event):
    if combobox3.get () == "ReadOnly":
        table_entry.grid (row=1,column=10,columnspan=2,sticky="w")
        tabel_create.grid (row=0,column=10,padx=0,pady=10,columnspan=1,sticky="w")
        table_entry.configure (state='readonly')

    elif combobox3.get () == "Table-input":
        table_entry.grid (row=1,column=10,columnspan=2,sticky="w")
        tabel_create.grid_forget ()

        text_var = []
        entries = []

        def get_mat():
            matrix = []
            for i in range (rows):
                matrix.append ([])
                for j in range (cols):
                    matrix[i].append (text_var[i][j].get ())

            print (type (matrix))

            table_text.set (matrix)

        Label (window,text="Abeceda 6x6 :",font=('arial',10,'bold'),
               bg="bisque2").place (x=360,y=80)

        x2 = 0
        y2 = 0

        rows,cols = (6,6)

        for i in range (rows):
            # append an empty list to your two arrays
            # so you can append to those later
            text_var.append ([])
            entries.append ([])
            for j in range (cols):
                # append your StringVar and Entry
                text_var[i].append (StringVar ())
                entries[i].append (Entry (window,textvariable=text_var[i][j],width=3))
                entries[i][j].place (x=360 + x2,y=100 + y2)
                x2 += 30

            y2 += 30
            x2 = 0
        button = Button (window,text="Submit",bg='bisque3',width=15,command=get_mat)
        button.place (x=360,y=280)

    elif combobox3.get () == "Textbox-input":
        table_entry.configure (state='normal')
        table_entry.grid (row=1,column=10,columnspan=2,sticky="w")
        tabel_create.grid_forget ()


pf = ADFGX ()
vg = ADFGVX ()
window = Tk ()

window.title ('ADFGVX šifra')
window.geometry ("600x320")

Label (window,text='Type').grid (row=0,column=0,padx=7,pady=5,sticky="w")
combobox1 = Combobox (window,
                      values=(
                          '5x5','6x6'
                      ),state='readonly',width=10)
combobox1.grid (row=0,column=1,sticky="w",pady=5)
combobox1.set ("5x5")
combobox1.bind ('<<ComboboxSelected>>',type_change)

combobox2 = Combobox (window,
                      values=(
                          'CZ','EN'
                      ),state='readonly',width=10)
combobox2.grid (row=0,column=2,sticky="w",pady=5,padx=10,columnspan=2)
combobox2.set ("EN")
combobox2.bind ('<<ComboboxSelected>>')

combobox3 = Combobox (window,
                      values=(
                          'ReadOnly','Table-input','Textbox-input'
                      ),state='readonly',width=10)
combobox3.grid (row=0,column=11,sticky="w",pady=5,padx=10,columnspan=2)
combobox3.set ("ReadOnly")
combobox3.bind ('<<ComboboxSelected>>',type_change1)

combobox4 = Combobox (window,
                      values=(
                          'Šifrovat','Dešifrovat'
                      ),state='readonly',width=10)
combobox4.grid (row=4,column=0,sticky="w",pady=5,padx=10,columnspan=2)
combobox4.set ("Šifrovat")
combobox4.bind ('<<ComboboxSelected>>')

Label (window,text='Klíč').grid (row=1,column=0,padx=7,pady=5,sticky="w")
key_text = StringVar ()
key_entry = Entry (window,textvariable=key_text,width=13)
key_entry.grid (row=1,column=1,sticky="w")

first_label = Label (window,text='Text')
first_label.grid (row=2,column=0,padx=7,pady=5,columnspan=2,sticky="w")
before_text = StringVar ()
before_entry = Entry (window,textvariable=before_text,width=24)
before_entry.grid (row=3,column=0,columnspan=2,padx=10,sticky="w")

second_label = Label (window,text='Zašifrovaný text')
second_label.grid (row=2,column=2,padx=0,pady=5,columnspan=2,sticky="w")
after_text = StringVar ()
after_entry = Entry (window,textvariable=after_text,width=30)
after_entry.grid (row=3,column=2,columnspan=2,sticky="w")

table_text = StringVar ()
table_entry = Entry (window,textvariable=table_text,state='readonly',width=40)
table_entry.grid (row=1,column=10,columnspan=2,sticky="w")


def random_char(y):
    if combobox1.get () == "5x5":
        mylist = string.ascii_lowercase
    elif combobox1.get () == "6x6":
        mylist = string.ascii_lowercase + string.digits

    a = random.sample (mylist,y)
    print (a)
    return a


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1


def onclick_table():
    if combobox1.get () == '5x5':
        table = random_char (25)
        table1 = listToString (table)
        table_text.set (table1)
    elif combobox1.get () == '6x6':
        table = random_char (36)
        table1 = listToString (table)
        table_text.set (table1)


def OsetriKlic(klic):
    diakritika = {"Á":"A","Č":"C","É":"E","Ě":"E","Ď":"D","Í":"I","Ň":"N","Ó":"O","Ř":"R","Š":"S","Ť":"T","Ů":"U",
                  "Ú":"U","Ý":"Y","Ž":"Z"}
    osetrenyKlic = ""
    klic1 = re.sub ('[!,*)@#%(&$_?.^]','',klic)
    klic1.replace (" ","")
    klic2 = klic1.lower ()

    validniAbeceda = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X",
                          "Y","Z"]

    for i in klic2:

        if validniAbeceda.count (i) > 0:
            osetrenyKlic += i
        else:
            try:
                aaa = diakritika[i]
                osetrenyKlic += aaa
            except:
                pass
    return osetrenyKlic

def onclick_button():
    after_entry.configure (state='normal')

    if combobox4.get () == 'Šifrovat':
        if combobox1.get () == "5x5":

            if combobox3.get () == "Table-input":
                messagebox.showerror ('Error','Pro abecedu 6x6 jenom pro ADFGVX ')
            else:
                key = key_text.get ().replace (" ","")
                key1 = key.lower ()
                if key1.isalpha ():
                    after_text.set (pf.encode (before_text.get (),key_text.get (),table_text.get ()))
                else:
                    messagebox.showerror ('ValueError','Klíč musí obsahovat text !')

        elif combobox1.get () == "6x6":
            key = key_text.get ().replace (" ","")
            key1 = key.lower ()
            if key1.isalpha ():
                after_text.set (vg.encode (before_text.get (),key_text.get (),table_text.get ()))
        else:
            messagebox.showerror ('ValueError','Klíč musí obsahovat text!')

    if combobox4.get () == 'Dešifrovat':

        if combobox1.get () == "5x5":

            if combobox3.get () == "Table-input":

                messagebox.showerror ('Error','Pro abecedu 6x6 jenom pro ADFGVX ')

            else:

                key = key_text.get ().replace (" ","")

                key1 = key.lower ()

                if key1.isalpha ():

                    before_text.set (pf.decode (after_text.get (),key_text.get (),table_text.get ()))

                else:

                    messagebox.showerror ('ValueError','Klíč musí obsahovat text !')


        elif combobox1.get () == "6x6":

            key = key_text.get ().replace (" ","")

            key1 = key.lower ()

            if key1.isalpha ():
                before_text.set (vg.decode (after_text.get (),key_text.get (),table_text.get ()))

        else:

            messagebox.showerror ('ValueError','Klíč musí obsahovat text!')

#before_text.set (pf.decode (after_text.get (),key_text.get (),table_text.get ())) 5x5
#before_text.set (vg.decode (after_text.get (),key_text.get (),table_text.get ())) 6x6
# encrypt_button = Button(window, text='Zašifrovat', command=onclick_encrypt)
# encrypt_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky="w")

decrypt_button = Button (window,text='Šifrovat',command=onclick_button)
decrypt_button.grid (row=4,column=2,padx=0,pady=10,columnspan=2,sticky="w")

tabel_create = Button (window,text='Vygenerovat',command=onclick_table)
tabel_create.grid (row=0,column=10,padx=0,pady=10,columnspan=1,sticky="w")

window.mainloop ()
