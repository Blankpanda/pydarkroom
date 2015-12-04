# # testing cooldown structure
# async_result = pool.apply_async(get_user_input)
# uin = async_result.get()
#
# if uin == "1" and fire_off_cooldown:
#     fire_cooldown_timer.start()
#     fire_off_cooldown = False
#     print("used 1.")
#
# if fire_cooldown_timer.check() and fire_off_cooldown == False:
#     fire_off_cooldown = True
#     print("1 off cooldown")
#
# if uin == "2" and wood_off_cooldown:
#     wood_cooldown_timer.start()
#     wood_off_cooldown = False
#     print("used 2.")
#
# if wood_cooldown_timer.check() and wood_off_cooldown == False:
#     wood_off_cooldown = True
#     print("2 off cooldown")
#
# uin = get_user_input()
# if uin == "1":
#     wood_resource_counter = modifiers.change_modifier(wood_resource_counter, 3)
#     wood_resource_counter.accum_resource_counter(1)
#     print(wood_resource_counter.get_resource_counter())
#
# wood_resource_counter.accum_resource_counter(1)
# print(wood_resource_counter.get_resource_counter())
# uin = get_user_input()
# print(flame.get_intensity_state(flame.get_current_intensity()))
#
# if uin == "1":
#     flame.kindle(20)
#     flame_is_burning = True
# if flame.check_burn_time():
#     flame.start_burn()
#     flame.burn()
# print(flame.get_current_intensity())
#
