import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
dpg.create_context()
dpg.create_viewport(title='Squad Discord Message Database', width=1000, height=600)

demo.show_demo()

'''
with dpg.window(label="Example window"):
    dpg.add_text("Hello, world!")
    dpg.add_button(label="save")
    dpg.add_input_text(label="string", default_value="Quick Brown Fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
'''
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()