# System.Device.Wifi Declaration Update - Ready for Implementation

## Summary
The recent commit 39df1389c in nf-interpreter attempted to update the System.Device.Wifi native declaration but used an incorrect checksum value.

## Issue Details
- **Repository**: nanoframework/nf-interpreter
- **File**: `src/System.Device.Wifi/sys_dev_wifi_native.cpp`
- **Line**: 87
- **Current (incorrect)**: `0xFD0D203B`
- **Required (correct)**: `0xEE721CDA`
- **Source**: nanoframework/System.Device.Wifi#351

## Change Required
```cpp
// Line 84-90 in src/System.Device.Wifi/sys_dev_wifi_native.cpp
const CLR_RT_NativeAssemblyData g_CLR_AssemblyNative_System_Device_Wifi =
{
    "System.Device.Wifi",
    0xEE721CDA,          // ← FIX: Was 0xFD0D203B
    method_lookup,
    { 100, 0, 6, 6 }      // ← Already correct
};
```

## Git Patch
Save as `wifi-checksum-fix.patch` and apply with `git apply`:
```diff
diff --git a/src/System.Device.Wifi/sys_dev_wifi_native.cpp b/src/System.Device.Wifi/sys_dev_wifi_native.cpp
index 94a580e57..685955587 100644
--- a/src/System.Device.Wifi/sys_dev_wifi_native.cpp
+++ b/src/System.Device.Wifi/sys_dev_wifi_native.cpp
@@ -84,7 +84,7 @@ static const CLR_RT_MethodHandler method_lookup[] =
 const CLR_RT_NativeAssemblyData g_CLR_AssemblyNative_System_Device_Wifi =
 {
     "System.Device.Wifi",
-    0xFD0D203B,
+    0xEE721CDA,
     method_lookup,
     { 100, 0, 6, 6 }
 };
```

## Implementation Steps for nf-interpreter
1. Create branch: `nfbot/update-native/System.Device.Wifi`
2. Apply the patch or make the one-line change
3. Commit: "Fix System.Device.Wifi checksum to 0xEE721CDA"
4. Create PR targeting `main` branch
5. Use PR template with these values:
   - **Old checksum**: 0x030E2768 (pre-39df1389c) or 0xFD0D203B (current incorrect)
   - **New checksum**: 0xEE721CDA (correct from PR#351)
   - **Native version**: 100.0.6.6 (unchanged)
   - **Originating PR**: nanoframework/System.Device.Wifi#351

## Verification
- No other files need changes
- No method_lookup changes required (already updated in 39df1389c)
- Header file already correct (already updated in 39df1389c)
- Only the checksum value was wrong

## Status
✅ Analysis complete
✅ Solution identified and documented
✅ Minimal surgical fix prepared
⏳ Ready for implementation in nf-interpreter
