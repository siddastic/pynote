def clean(History):
    for i in History :
        i.pack_forget()
    History = []