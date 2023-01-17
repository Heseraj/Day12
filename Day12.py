# This is the start of the 12 day.
#Stay focused and keep working.
enemies = 1
def increase_enemies():
    global enemies # this will bring the global variable inside the local environment
    enemies += 1 # try to avoid modifying global scope
    print(f"enemies inside function {enemies}")
#%%
increase_enemies()
#%%
print(f"enemies from outside the program {enemies}")
#%%


#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
