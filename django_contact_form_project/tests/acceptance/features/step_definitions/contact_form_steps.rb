Given(/^User is on contact form page$/) do
    visit '/contact/'
    expect(page).to have_content('Contact Form')
end

When(/^User completes the form$/) do
    fill_in 'firstname', with: 'lnwBoss'
    fill_in 'lastname', with: 'yong'
end

When(/^User clicks submit button$/) do
    click_button 'Submit'
end

Then(/^User sees no error$/) do
    expect(page).not_to have_content('This field is required.')
end

When(/^User fills in only lastname$/) do
    fill_in 'lastname', with: 'yong'
end

Then(/^User sees error$/) do
    expect(page).to have_content('This field is required.')

end

When(/^User fills in only firstname$/) do
    fill_in 'firstname', with: 'lnwBoss'
end

Then(/^User should be redirected to thank you page$/) do
    expect(page).to have_content('Thank you')
    expect(page).to have_content('Firstname: lnwBoss')
    expect(page).to have_content('Lastname: yong')
end
