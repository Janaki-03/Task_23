from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the jQuery UI droppable page
driver.get("https://jqueryui.com/droppable/")

# Switch to the iframe containing the draggable elements
driver.switch_to.frame(0)  # Assuming there's only one iframe on the page

# Locate the draggable and droppable elements
draggable = driver.find_element(by=By.ID, value="draggable")
droppable = driver.find_element(by=By.ID, value="droppable")

# Create an ActionChains object to perform the drag-and-drop
actions = ActionChains(driver)

# Perform the drag-and-drop operation
actions.drag_and_drop(draggable, droppable).perform()

# You can also use this alternative approach for the drag-and-drop:
# actions.click_and_hold(draggable).move_to_element(droppable).release().perform()

# Close the browser
driver.quit()



