# Skeleton of an ansible module
For now it accepts just an argument: the *endpoint*.  
The module queries the endpoint, makes a couple of error checks,
then parses the json output in the body and returns a list of strings.

# Testing the module
After a git clone, enter the directory and
```
$ export ANSIBLE_LIBRARY=./library
```

At this point, you can hack on this module on your local ansible installation:
```bash
$ ansible localhost -m get_tokens -a 'endpoint="https://jsonplaceholder.typicode.com/posts/2"'
$ ansible-doc get_tokens
```

# Reference
The [Ansible module devel tutorial](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html)
