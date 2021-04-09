switcher = {
            'normal' : 'self.normal_color',
            'red' : 'self.red_color',
            'blue' : 'self.blue_color',
            'bomb' : 'self.bomb_color'
        }
txt = 'red'
print(switcher.get(txt.lower()))