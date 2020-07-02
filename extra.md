# Extra notes
## Plans and ideas
1. **Improve set_user_role() func in admin_commands**

**Now:** admin sets user role through digits (telegram_id and role_id)

**Task:** admin should set user role through telegram login and name of the role.

**Solution:** add new function to dao file. It should return login of the user.
Then add recognition of the role through keywords in function set_user_role()

2. **Strings refactoring**

**Task:** change all strings with .format() func to f-strings.

## Problems
1. **show_my_notifications() func in notification_commands**

**Problem:** Yet can't predict how notifications will be shown because of the foreign keys.

**Solution:** This problem will be resolved later, when tests will be started.