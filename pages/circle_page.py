from pages.base_page import Page
from selenium.webdriver.common.by import By


class CirclePage(Page):
    BENEFIT_CELL_COUNT = (By.XPATH, "//a[contains(@data-test, '@web/slingshot-components/CellsComponent/Link')]")

    def open_circle_page(self):
        self.driver.implicitly_wait(4)
        benefit_cell = self.find_elements(*self.BENEFIT_CELL_COUNT)
        assert len(benefit_cell) > 10, f"Expected at least 10 benefit cells, {len(benefit_cell)} cells found"