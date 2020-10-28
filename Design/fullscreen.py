def make(parent,hideDefault = False):
    width,height = parent.winfo_screenwidth(),parent.winfo_screenheight()
    parent.geometry(f"{width}x{height}")
    if(hideDefault):
        parent.overrideredirect(True)