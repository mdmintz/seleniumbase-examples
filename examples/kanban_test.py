""" Kanban board testing example """
from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_kanban_board(self):
        self.open("https://cryptpad.fr/kanban/")
        self.switch_to_frame("iframe#sbox-iframe")
        self.click("button.cp-corner-cancel", timeout=15)
        self.click("span.cp-help-close")

        self.delete_all_boards()
        self.add_board("To Do")
        self.add_board("In progress")
        self.add_board("Done")
        self.set_board_data()
        self.click("div.cp-corner-dontshow span.fa", timeout=15)

        self.add_item_to_board("Item 1", "To Do")
        self.add_item_to_board("Item 2", "To Do")
        self.add_item_to_board("Item 3", "To Do")
        self.add_item_to_board("Item 4", "To Do")
        self.add_item_to_board("Item 5", "To Do")
        self.add_item_to_board("Item 6", "To Do")

        self.move_item_to_board("Item 4", "In progress")
        self.move_item_to_board("Item 3", "In progress")
        self.move_item_to_board("Item 6", "Done")
        self.move_item_to_board("Item 5", "Done")

        self.set_board_data()
        for b_name in self.board_data.keys():
            self.assert_text(
                b_name, 'div[data-id="%s"]' % self.board_data[b_name][0])
        for item_name in self.all_items.keys():
            self.assert_text(
                item_name, 'div[data-eid="%s"]' % self.all_items[item_name][0])

    def set_board_data(self, soup=None, get=False):
        board_data = {}  # Dictionary -> {name: (data_id, position)}
        board_items = {}  # Dictionary -> {name: {item_name: (item_id, i_pos)}}
        all_items = {}  # Dictionary -> {item_name: (item_id, i_pos, b_pos)}
        count = 0
        if not soup:
            soup = self.get_beautiful_soup()
        divs = soup.body.find_all("div")
        for div in divs:
            item_data = {}
            item_position = 0
            if div.get("class") and div.get("class")[0] == "kanban-board":
                board_data[div.header.text] = (div.get("data-id"), count)
                item_divs = div.main.find_all("div")
                for i_d in item_divs:
                    if i_d.get("class"):
                        if i_d.get("class")[0] == "kanban-item":
                            i_name = i_d.text
                            i_id = i_d.get("data-eid")
                            i_position = item_position
                            item_position += 1
                            item_data[i_name] = (i_id, i_position)
                            all_items[i_name] = (i_id, i_position, count)
                board_items[div.header.text] = item_data
                count += 1
        self.board_data = board_data
        self.board_items = board_items
        self.all_items = all_items
        if get:
            return board_data, board_items, all_items

    def delete_all_boards(self):
        for i in range(8):
            if self.is_element_visible('[alt="Edit this board"]'):
                self.click('[alt="Edit this board"]')
                self.click('button.danger')
                self.click('div.cp-button-confirm')

    def add_board(self, name):
        self.click("#kanban-addboard")
        num_boards = len(self.find_visible_elements('[alt="Edit this board"]'))
        self.click_nth_visible_element('[alt="Edit this board"]', num_boards)
        self.type("input#cp-kanban-edit-title", name)
        self.click("button.primary")

    def add_item_to_board(self, name, board):
        board_id = self.board_data[board][0]
        self.sleep(0.1)
        self.click('div[data-id="%s"] i.cptools-add-bottom' % board_id)
        self.sleep(0.1)
        self.click('input#kanban-edit')
        self.type('input#kanban-edit', name)
        self.click(".cp-toolbar-spinner")

    def move_item_to_board(self, name, board):
        self.set_board_data()
        board_position = self.board_data[board][1]
        item_id = self.all_items[name][0]
        item_x_position = self.all_items[name][2]
        item_y_position = self.all_items[name][1]
        x_offset = (board_position - item_x_position) * 350
        y_offset = (0 - item_y_position) * 46
        self.drag_and_drop_with_offset(
            'div[data-eid="%s"]' % item_id, x_offset, y_offset)
