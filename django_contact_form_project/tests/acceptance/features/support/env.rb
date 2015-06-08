require 'capybara/cucumber'
require 'selenium-webdriver'
require 'headless'
Capybara.default_driver = :selenium
headless = Headless.new(:dimensions => '1920x1080x24')
headless.start
Capybara.configure do |config|
    config.app_host = 'http://192.168.1.111:3000'
end
