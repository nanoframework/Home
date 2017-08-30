# Guidelines for debugging **nanoFramework** class libraries native code

**About this document**

This document provides guidelines useful when debugging class libraries native code.
It doesn't care if the developer is using VS Code or other IDE.


## How does an assembly load successfully?

The assemblies with the class libraries and the managed application are loaded at startup from the deployment area in the FLASH memory.
When the `LoadDeploymentAssemblies()` is called the deployment area is sweep and all 'candidate' assemblies are validated. The validation steps are basically checking the start token, a valid header and the CRC32 of the full assembly. Only the ones that pass the complete set of validation make it to the assembly collection.

After this step a call to `g_CLR_RT_TypeSystem.ResolveAll()` happens in which the type system tries to resolve all the assemblies. This means that all the required types and methods (from all the assemblies) are available and in the correct versions.

Next comes the `g_CLR_RT_TypeSystem.PrepareForExecution()` which is only called if all the assemblies could be resolved along with the required types.


## Starting the execution engine

The managed application actually starts to be executed with a call to `g_CLR_RT_ExecutionEngine.Execute()`.
As long the managed code is being executed this will never exit.
When the execution ends, because of a serious exception or because there is no managed application to execute the code flow hits the `CLR_EE_DBG_IS( RebootPending )` line (bellow the the call to the execution engine call).


## Summarizing

So, by setting break points at, or after, the above calls one can understand and perform a check if the assemblies are being loaded and/or the managed application being executed.
If something goes wrong (for instance) with an assembly failing to load the developer has to go deeper in order to find out the root cause. But that's a matter for another piece of documentation.
