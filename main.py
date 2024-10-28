def on_forever():
    if input.temperature() > 22:
        basic.show_string("calor")
    else:
        basic.show_string("fred")
    if input.temperature() > 22:
        basic.show_string("calor")
    else:
        basic.show_string("fred")
basic.forever(on_forever)
