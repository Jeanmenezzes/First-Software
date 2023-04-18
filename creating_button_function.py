# This function will be charged to create buttons widgets and return them
import PIL.Image as Image
import PIL.ImageTk as ImageTk
import functools
import tkinter
import pdb


# Create a new button with an image address
def new_button(image_address, frame, main_color, variable):
    # The button will grow and decrease based in a resize factor
    #pdb.set_trace()
    image_pil = Image.open(image_address)
    resize_factor = (int(image_pil.size[0]*1.1), int(image_pil.size[1]*1.1))

    image_tk = ImageTk.PhotoImage(image=image_pil)
    image_tk_rz = ImageTk.PhotoImage(image=image_pil.resize(resize_factor))

    label_button = tkinter.Label(frame, image=image_tk, bg=main_color, width=resize_factor[0] + 4,
                                 height=resize_factor[1] + 4)

    # This part is responsible to fix the borders tax what the label put
    if image_pil.size[0] == 150:
        fix_tax = (9, 13)
    elif image_pil.size[0] == 50:
        fix_tax = (6, 6)

    # A list contain all image's coordinates what trigger the button
    pixel_img = [[x, y] for x in range(1, image_pil.size[0]) for y in range(1, image_pil.size[1])
                 if image_pil.getpixel((x, y)) != (0, 0, 0, 0)]

    # This function uses the coordinates to trigger the increase image and the button function command
    def func(event, widget=None, pixel_list=None, image_1=None, image_2=None, var=None, name=None):
        x = widget.winfo_pointerxy()[0] - widget.winfo_rootx() - fix_tax[0]
        y = widget.winfo_pointerxy()[1] - widget.winfo_rooty() - fix_tax[1]

        if [x, y] in pixel_list:
            if int(event.type) == 4:
                widget.configure(image=image_2)
                try:
                    var.name = image_address[7:].replace('_ico.png', '')
                except AttributeError:
                    pass
            elif int(event.type) == 5:
                widget.configure(image=image_1)
                var.set(True)

    # The button is bind to Button-1 with the function func, what animate and changes the variable var
    label_button.bind('<Button-1>', functools.partial(func, widget=label_button, pixel_list=pixel_img, image_1=image_tk,
                                                      image_2=image_tk_rz, var=variable))
    label_button.bind('<ButtonRelease-1>', functools.partial(func, widget=label_button, pixel_list=pixel_img,
                                                             image_1=image_tk, image_2=image_tk_rz, var=variable))

    return label_button
