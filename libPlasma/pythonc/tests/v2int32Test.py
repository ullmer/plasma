import plasma

v2 = plasma.v2int32(43, -129)  # Create a v2int32 vector
sv2 = plasma.Slaw(v2)          # Wrap it in a Slaw
v22 = sv2.Emit(plasma.v2int32) # Emit it back to v2int32
sv2.Spew()                     # Step 4: Print the Slaw

