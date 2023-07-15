# Debing-KICKS
![](https://www.jaymoseley.com/hercules/kicks/images/kicks_startup_2.png)

## Synopsis
Debian-KICKS is a fully orchestrated Docker container for TurnKey (TK4) MVS KICKS.

## Assumptions
* There is a need to containerize a KICKS TK4 system.
* It is possible to interact with TK4 outside of the TSO prompt.
* Installing the KICKS environment will only need to be done once on initial run.
* There is no need to uninstall KICKS.
* The container should alo be able to be used for batch processing.
* Common libraries and tools will be installed on the Debian layer.

## Requirements
* The container must be able to install and load KICKS without manual intervention.
* The container must be able to be used for batch processing.
* The container must be sharable and fully open-sourced.

## Constraints
* The container must support Docker build 114176 (or higher).
* The container must support Debian 11 (or higher).
* The container must be runnable with 47 GB or more (Docker disk).
* The container must be runnable with 2 GB or more (Docker RAM).
* The container must be runnable with 1 GB or more (Docker swappable).

## Implementation Details
The implementation takes an existing orchestration and automates the manual process of loading in the KICKS XMIT through a bootstrap script when running the container.  The bootstrapping is done through the Makefile, so it's absolutely important to instrument the container through the given utilities.  The bootstrapper initializes the XMIT by telling Hercules to take it in in the card reader via an HTTP call to Hercules.  We then start to load in the PDS through telnet calls to MVS.  The only thing that's left once the container is created is to startup KICKS under the HERC01 user.

## References

