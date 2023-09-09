# Skeleton of an ansible module
For now it accepts just an argument: the *endpoint*.  
The module queries the endpoint, makes a couple of error checks,
then parses the json output in the body and returns a list of strings.

## part of a collection
To make the module distributable, it has been added to an ansible collection.

From the toplevel dir in the repo:
```bash
# build the collection tarball
$ ansible-galaxy collection build ./andrewdomain/custom_modules/

# to install the collection locally
$ ansible-galaxy collection install ./andrewdomain/custom_modules/
```

The collection is then saved (depending on the system you're using) in *~/.ansible/collections/*  
A simple *rm -rf ~/.ansible/collections/andrewdomain* should be enough to "uninstall" it.

# Testing the module
After installing the collection (see above).

```bash
$ ansible localhost -m andrewdomain.custom_modules.get_tokens -a 'endpoint="https://jsonplaceholder.typicode.com/posts/2"'
$ ansible-doc andrewdomain.custom_modules.get_tokens
```

At this point, you can hack on this module on your local ansible installation.  
The module's source is in (from the toplevel) *andrewdomain/custom_modules/plugins/modules/*

# Reference
 + The [Ansible module devel tutorial](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html)
 + The [Ansible collection devel docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html)
 + Also *ls -l ~/.ansible/collections* (if you have any) to see what goes where..
