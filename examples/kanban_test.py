""" Kanban board testing example """
from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    popup_removed = False

    def test_kanban_board(self):
        self.open("https://cryptpad.fr/kanban/")
        self.switch_to_frame("iframe#sbox-iframe")
        self.click("button.cp-corner-cancel", timeout=30)
        self.click("div.cp-corner-dontshow span")

        self.delete_all_boards()
        self.add_board("To Do")
        self.add_board("In progress")
        self.add_board("Done")
        self.set_board_data()

        if not self.popup_removed:
            self.sleep(1)
            print("Waiting to close pop-up...")
            if self.is_element_visible("div.cp-corner-dontshow span"):
                self.sleep(0.1)
                self.click("div.cp-corner-dontshow span")
                print("Pop-up closed!")
                self.sleep(0.3)

        # Add items to the first board
        self.add_item_to_board("Item 1", "To Do")
        self.add_item_to_board("Item 2", "To Do")
        self.add_item_to_board("Item 3", "To Do")
        self.add_item_to_board("Item 4", "To Do")
        self.add_item_to_board("Item 5", "To Do")
        self.add_item_to_board("Item 6", "To Do")

        # Drag and drop items onto different boards
        self.move_item_to_board("Item 4", "In progress")
        self.move_item_to_board("Item 3", "In progress")
        self.move_item_to_board("Item 6", "Done")
        self.move_item_to_board("Item 5", "Done")

        # Verify boards and items
        self.set_board_data()
        for b_name in self.board_data.keys():
            self.assert_text(
                b_name, 'div[data-id="%s"]' % self.board_data[b_name][0])
        for item_name in self.all_items.keys():
            self.assert_text(
                item_name, 'div[data-eid="%s"]' % self.all_items[item_name][0])

        # Verify the visibility status of the kanban trash from class changes
        self.set_attribute(
            '#kanban-trash', 'class', 'kanban-trash kanban-trash-suggest')
        self.assert_element_visible('#kanban-trash')
        self.set_attribute(
            '#kanban-trash', 'class', 'kanban-trash kanban-trash-active')
        self.assert_element_visible('#kanban-trash')
        self.set_attribute('#kanban-trash', 'class', 'kanban-trash')
        self.assert_element_not_visible('#kanban-trash')

    def remove_popup_if_visible(self):
        if self.is_element_visible("div.cp-corner-dontshow span"):
            self.click("div.cp-corner-dontshow span")
            self.popup_removed = True
            self.sleep(0.3)

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
        self.remove_popup_if_visible()
        for i in range(8):
            if self.is_element_visible('[alt="Edit this board"]'):
                self.click('[alt="Edit this board"]')
                self.click('button.danger')
                self.click('div.cp-button-confirm')
                self.sleep(0.1)

    def add_board(self, name):
        self.sleep(0.2)
        self.remove_popup_if_visible()
        self.click("#kanban-addboard")
        self.sleep(0.4)
        self.remove_popup_if_visible()
        num_boards = len(self.find_visible_elements('[alt="Edit this board"]'))
        self.sleep(0.1)
        self.remove_popup_if_visible()
        self.sleep(0.2)
        self.click_nth_visible_element('[alt="Edit this board"]', num_boards)
        self.sleep(0.4)
        self.remove_popup_if_visible()
        self.sleep(0.2)
        self.type("input#cp-kanban-edit-title", name)
        self.sleep(0.4)
        self.remove_popup_if_visible()
        self.click("button.primary")
        self.sleep(0.2)
        self.assert_element('div.kanban-title-board:contains("%s")' % name)

    def add_item_to_board(self, name, board):
        self.remove_popup_if_visible()
        board_id = self.board_data[board][0]
        self.sleep(0.2)
        self.remove_popup_if_visible()
        self.wait_for_element(
            'div[data-id="%s"] i.cptools-add-bottom' % board_id)
        self.sleep(0.05)
        self.remove_popup_if_visible()
        self.js_click('div[data-id="%s"] i.cptools-add-bottom' % board_id)
        self.sleep(0.3)
        self.js_type('input#kanban-edit', name)
        self.sleep(0.2)
        self.click(".cp-toolbar-spinner")

    def move_item_to_board(self, name, board):
        self.remove_popup_if_visible()
        self.set_board_data()
        board_position = self.board_data[board][1]
        item_id = self.all_items[name][0]
        item_x_position = self.all_items[name][2]
        item_y_position = self.all_items[name][1]
        x_offset = (board_position - item_x_position) * 350
        y_offset = (0 - item_y_position) * 46
        self.drag_and_drop_with_offset(
            'div[data-eid="%s"]' % item_id, x_offset, y_offset)
