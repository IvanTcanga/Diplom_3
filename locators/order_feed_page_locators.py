from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
	UL_ORDER_FEED = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]') # Список всех заказов

	TITLE_ORDER_FEED = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1') # Заголовок "Лента заказов"

	FIRST_BURGER_CARD = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')

	MODAL_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_orderBox")]') #модальное окно с заказом

	TITLE_MODAL_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_orderBox")]//h2') # Заголовок модального окна

	ALL_ORDERS_QUANTITY = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p') # Всего заказов

	TODAY_ORDERS_QUANTITY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p') #Заказы сегодня

	ORDER_LIST_READY = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li') # заказы в работе

	#искомый заказ
	# TARGET_ORDER_READY_IN_UL = (By.XPATH, f'//ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(text(), "{order_number}")]')

	NUMBER_OF_ORDER = (By.XPATH, '//li[contains(@class, "text_type_digits-default")]') # Номер заказа
	# // div[ @
	#
	# class ='OrderFeed_ordersData__1L6Iv'] // li[3]
	# # Номер заказа в ленте — заготовка, в которую нужно подставить id искомого заказа
	# id_order_card_in_feed_with_substitutions = (By.XPATH, './/*[text()="{order_id}"]')