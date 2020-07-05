# Extra notes
## Plans and ideas
1. **Improve set_user_role() func in admin_commands**

**Now:** admin sets user role through digits (telegram_id and role_id)

**Task:** admin should set user role through telegram login and name of the role.

**Solution:** add new function to dao file. It should return login of the user.
Then add recognition of the role through keywords in function set_user_role()

- [X] PARTLY SOLVED

2. **Strings refactoring**

**Task:** change all strings with .format() func to f-strings.

3. **Change formatting of SQLalchemy objects to json**

**Task:** change formatting in db_classes and improve dao module.

## Problems
1. **show_my_notifications() func in notification_commands**

**Problem:** yet can't predict how notifications will be shown because of the foreign keys.

**Solution:** this problem will be resolved later, when tests will be started.

2. **Add new test functions**

**Problem:** new functions were added to dao module, but none of them have been tested yet.

**Solution:** just do it.

- [X] SOLVED