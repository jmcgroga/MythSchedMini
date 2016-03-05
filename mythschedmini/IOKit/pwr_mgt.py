from __future__ import print_function

import ctypes
import objc

#gen_bridge_metadata -c '-l/System/Library/Frameworks/IOKit.framework/IOKit -I/System/Library/Frameworks/IOKit.framework/Headers/pwr_mgt/' `find /System/Library/Frameworks/IOKit.framework/Headers/pwr_mgt -name \*.h -print0 | xargs -0` -o pwr_mgt.xml

GEN_BRIDGE_METADATA ="""<?xml version='1.0'?>
<!DOCTYPE signatures SYSTEM "file://localhost/System/Library/DTDs/BridgeSupport.dtd">
<signatures version='1.0'>
  <struct name='IOPMCalendarStruct' type='{IOPMCalendarStruct=&quot;year&quot;I&quot;month&quot;C&quot;day&quot;C&quot;hour&quot;C&quot;minute&quot;C&quot;second&quot;C&quot;selector&quot;C}'/>
  <struct name='IOPMSystemCapabilityChangeParameters' type='{IOPMSystemCapabilityChangeParameters=&quot;notifyRef&quot;I&quot;maxWaitForReply&quot;I&quot;changeFlags&quot;I&quot;__reserved1&quot;I&quot;fromCapabilities&quot;I&quot;toCapabilities&quot;I&quot;__reserved2&quot;[4I]}'/>
  <struct name='IOPowerStateChangeNotification' type='{IOPowerStateChangeNotification=&quot;powerRef&quot;^v&quot;returnValue&quot;L&quot;stateNumber&quot;L&quot;stateFlags&quot;I}' type64='{IOPowerStateChangeNotification=&quot;powerRef&quot;^v&quot;returnValue&quot;Q&quot;stateNumber&quot;Q&quot;stateFlags&quot;Q}'/>
  <struct name='sleepWakeNote' type='{IOPowerStateChangeNotification=&quot;powerRef&quot;^v&quot;returnValue&quot;L&quot;stateNumber&quot;L&quot;stateFlags&quot;I}' type64='{IOPowerStateChangeNotification=&quot;powerRef&quot;^v&quot;returnValue&quot;Q&quot;stateNumber&quot;Q&quot;stateFlags&quot;Q}'/>
  <string_constant name='kAppleClamshellCausesSleepKey' value='AppleClamshellCausesSleep'/>
  <string_constant name='kAppleClamshellStateKey' value='AppleClamshellState'/>
  <string_constant name='kIOBatteryAmperageKey' value='Amperage'/>
  <string_constant name='kIOBatteryCapacityKey' value='Capacity'/>
  <string_constant name='kIOBatteryCurrentChargeKey' value='Current'/>
  <string_constant name='kIOBatteryCycleCountKey' value='Cycle Count'/>
  <string_constant name='kIOBatteryFlagsKey' value='Flags'/>
  <string_constant name='kIOBatteryInfoKey' value='IOBatteryInfo'/>
  <string_constant name='kIOBatteryVoltageKey' value='Voltage'/>
  <string_constant name='kIOPMAssertNetworkClientActive' nsstring='true' value='NetworkClientActive'/>
  <string_constant name='kIOPMAssertPreventDiskIdle' nsstring='true' value='PreventDiskIdle'/>
  <string_constant name='kIOPMAssertPreventUserIdleDisplaySleep' nsstring='true' value='PreventUserIdleDisplaySleep'/>
  <string_constant name='kIOPMAssertPreventUserIdleSystemSleep' nsstring='true' value='PreventUserIdleSystemSleep'/>
  <string_constant name='kIOPMAssertionDetailsKey' nsstring='true' value='Details'/>
  <string_constant name='kIOPMAssertionFrameworkIDKey' nsstring='true' value='FrameworkBundleID'/>
  <string_constant name='kIOPMAssertionHumanReadableReasonKey' nsstring='true' value='HumanReadableReason'/>
  <string_constant name='kIOPMAssertionLevelKey' nsstring='true' value='AssertLevel'/>
  <string_constant name='kIOPMAssertionLocalizationBundlePathKey' nsstring='true' value='BundlePath'/>
  <string_constant name='kIOPMAssertionNameKey' nsstring='true' value='AssertName'/>
  <string_constant name='kIOPMAssertionPlugInIDKey' nsstring='true' value='PlugInBundleID'/>
  <string_constant name='kIOPMAssertionRetainCountKey' nsstring='true' value='RetainCount'/>
  <string_constant name='kIOPMAssertionTimeoutActionKey' nsstring='true' value='TimeoutAction'/>
  <string_constant name='kIOPMAssertionTimeoutActionLog' nsstring='true' value='TimeoutActionLog'/>
  <string_constant name='kIOPMAssertionTimeoutActionRelease' nsstring='true' value='TimeoutActionRelease'/>
  <string_constant name='kIOPMAssertionTimeoutActionTurnOff' nsstring='true' value='TimeoutActionTurnOff'/>
  <string_constant name='kIOPMAssertionTimeoutKey' nsstring='true' value='TimeoutSeconds'/>
  <string_constant name='kIOPMAssertionTypeKey' nsstring='true' value='AssertType'/>
  <string_constant name='kIOPMAssertionTypeNoDisplaySleep' nsstring='true' value='NoDisplaySleepAssertion'/>
  <string_constant name='kIOPMAssertionTypeNoIdleSleep' nsstring='true' value='NoIdleSleepAssertion'/>
  <string_constant name='kIOPMAssertionTypePreventSystemSleep' nsstring='true' value='PreventSystemSleep'/>
  <string_constant name='kIOPMAssertionsDriverDetailedKey' value='DriverPMAssertionsDetailed'/>
  <string_constant name='kIOPMAssertionsDriverKey' value='DriverPMAssertions'/>
  <string_constant name='kIOPMAutoPowerOn' value='poweron'/>
  <string_constant name='kIOPMAutoRestart' value='restart'/>
  <string_constant name='kIOPMAutoShutdown' value='shutdown'/>
  <string_constant name='kIOPMAutoSleep' value='sleep'/>
  <string_constant name='kIOPMAutoWake' value='wake'/>
  <string_constant name='kIOPMAutoWakeOrPowerOn' value='wakepoweron'/>
  <string_constant name='kIOPMBatteryChargeStatusGradient' value='BatteryTemperatureGradient'/>
  <string_constant name='kIOPMBatteryChargeStatusTooCold' value='LowTemperature'/>
  <string_constant name='kIOPMBatteryChargeStatusTooHot' value='HighTemperature'/>
  <string_constant name='kIOPMBatteryChargeStatusTooHotOrCold' value='HighOrLowTemperature'/>
  <string_constant name='kIOPMBootSessionUUIDKey' value='BootSessionUUID'/>
  <string_constant name='kIOPMCPUPowerLimitProcessorCountKey' value='CPU_Available_CPUs'/>
  <string_constant name='kIOPMCPUPowerLimitProcessorSpeedKey' value='CPU_Speed_Limit'/>
  <string_constant name='kIOPMCPUPowerLimitSchedulerTimeKey' value='CPU_Scheduler_Limit'/>
  <string_constant name='kIOPMCPUPowerLimitsKey' value='CPU_Power_Limits'/>
  <string_constant name='kIOPMCPUPowerNotificationKey' value='com.apple.system.power.CPU'/>
  <string_constant name='kIOPMDeepSleepDelayKey' value='Standby Delay'/>
  <string_constant name='kIOPMDeepSleepEnabledKey' value='Standby Enabled'/>
  <string_constant name='kIOPMDestroyFVKeyOnStandbyKey' value='DestroyFVKeyOnStandby'/>
  <string_constant name='kIOPMDeviceNameKey' value='DeviceName'/>
  <string_constant name='kIOPMDriverAssertionAssertedKey' value='Assertions'/>
  <string_constant name='kIOPMDriverAssertionCreatedTimeKey' value='CreatedTime'/>
  <string_constant name='kIOPMDriverAssertionIDKey' value='ID'/>
  <string_constant name='kIOPMDriverAssertionLevelKey' value='Level'/>
  <string_constant name='kIOPMDriverAssertionModifiedTimeKey' value='ModifiedTime'/>
  <string_constant name='kIOPMDriverAssertionOwnerServiceKey' value='ServicePtr'/>
  <string_constant name='kIOPMDriverAssertionOwnerStringKey' value='Owner'/>
  <string_constant name='kIOPMDriverAssertionRegistryEntryIDKey' value='RegistryEntryID'/>
  <string_constant name='kIOPMFullyChargedKey' value='FullyCharged'/>
  <string_constant name='kIOPMGraphicsPowerLimitPerformanceKey' value='Graphics_Power_Performance'/>
  <string_constant name='kIOPMGraphicsPowerLimitsKey' value='Graphics_Power_Limits'/>
  <string_constant name='kIOPMPSAdapterDetailsAmperageKey' value='Amperage'/>
  <string_constant name='kIOPMPSAdapterDetailsDescriptionKey' value='Description'/>
  <string_constant name='kIOPMPSAdapterDetailsFamilyKey' value='FamilyCode'/>
  <string_constant name='kIOPMPSAdapterDetailsIDKey' value='AdapterID'/>
  <string_constant name='kIOPMPSAdapterDetailsKey' value='AdapterDetails'/>
  <string_constant name='kIOPMPSAdapterDetailsPMUConfigurationKey' value='PMUConfiguration'/>
  <string_constant name='kIOPMPSAdapterDetailsRevisionKey' value='AdapterRevision'/>
  <string_constant name='kIOPMPSAdapterDetailsSerialNumberKey' value='SerialNumber'/>
  <string_constant name='kIOPMPSAdapterDetailsWattsKey' value='Watts'/>
  <string_constant name='kIOPMPSAdapterInfoKey' value='AdapterInfo'/>
  <string_constant name='kIOPMPSAmperageKey' value='Amperage'/>
  <string_constant name='kIOPMPSAtCriticalLevelKey' value='AtCriticalLevel'/>
  <string_constant name='kIOPMPSAtWarnLevelKey' value='AtWarnLevel'/>
  <string_constant name='kIOPMPSBatteryChargeStatusKey' value='ChargeStatus'/>
  <string_constant name='kIOPMPSBatteryHealthKey' value='BatteryHealth'/>
  <string_constant name='kIOPMPSBatteryInstalledKey' value='BatteryInstalled'/>
  <string_constant name='kIOPMPSBatteryTemperatureKey' value='Temperature'/>
  <string_constant name='kIOPMPSCapacityEstimatedKey' value='CapacityEstimated'/>
  <string_constant name='kIOPMPSChargerConfigurationKey' value='ChargerConfiguration'/>
  <string_constant name='kIOPMPSCurrentCapacityKey' value='CurrentCapacity'/>
  <string_constant name='kIOPMPSCycleCountKey' value='CycleCount'/>
  <string_constant name='kIOPMPSDesignCapacityKey' value='DesignCapacity'/>
  <string_constant name='kIOPMPSErrorConditionKey' value='ErrorCondition'/>
  <string_constant name='kIOPMPSExternalChargeCapableKey' value='ExternalChargeCapable'/>
  <string_constant name='kIOPMPSExternalConnectedKey' value='ExternalConnected'/>
  <string_constant name='kIOPMPSHealthConfidenceKey' value='HealthConfidence'/>
  <string_constant name='kIOPMPSInvalidWakeSecondsKey' value='BatteryInvalidWakeSeconds'/>
  <string_constant name='kIOPMPSIsChargingKey' value='IsCharging'/>
  <string_constant name='kIOPMPSLegacyBatteryInfoKey' value='LegacyBatteryInfo'/>
  <string_constant name='kIOPMPSLocationKey' value='Location'/>
  <string_constant name='kIOPMPSManufactureDateKey' value='ManufactureDate'/>
  <string_constant name='kIOPMPSManufacturerKey' value='Manufacturer'/>
  <string_constant name='kIOPMPSMaxCapacityKey' value='MaxCapacity'/>
  <string_constant name='kIOPMPSMaxErrKey' value='MaxErr'/>
  <string_constant name='kIOPMPSModelKey' value='Model'/>
  <string_constant name='kIOPMPSPostChargeWaitSecondsKey' value='PostChargeWaitSeconds'/>
  <string_constant name='kIOPMPSPostDishargeWaitSecondsKey' value='PostDischargeWaitSeconds'/>
  <string_constant name='kIOPMPSSerialKey' value='Serial'/>
  <string_constant name='kIOPMPSTimeRemainingKey' value='TimeRemaining'/>
  <string_constant name='kIOPMPSVoltageKey' value='Voltage'/>
  <string_constant name='kIOPMPowerEventAppNameKey' value='scheduledby'/>
  <string_constant name='kIOPMPowerEventTimeKey' value='time'/>
  <string_constant name='kIOPMPowerEventTypeKey' value='eventtype'/>
  <string_constant name='kIOPMResetPowerStateOnWakeKey' value='IOPMResetPowerStateOnWake'/>
  <string_constant name='kIOPMSettingAutoPowerCalendarKey' value='PowerByCalendarDate'/>
  <string_constant name='kIOPMSettingAutoPowerSecondsKey' value='poweron'/>
  <string_constant name='kIOPMSettingAutoWakeCalendarKey' value='WakeByCalendarDate'/>
  <string_constant name='kIOPMSettingAutoWakeSecondsKey' value='wake'/>
  <string_constant name='kIOPMSettingDebugPowerRelativeKey' value='PowerRelativeToShutdown'/>
  <string_constant name='kIOPMSettingDebugWakeRelativeKey' value='WakeRelativeToSleep'/>
  <string_constant name='kIOPMSettingDisplaySleepUsesDimKey' value='Display Sleep Uses Dim'/>
  <string_constant name='kIOPMSettingGraphicsSwitchKey' value='GPUSwitch'/>
  <string_constant name='kIOPMSettingMaintenanceWakeCalendarKey' value='MaintenanceWakeCalendarDate'/>
  <string_constant name='kIOPMSettingMobileMotionModuleKey' value='MobileMotionModule'/>
  <string_constant name='kIOPMSettingReduceBrightnessKey' value='ReduceBrightness'/>
  <string_constant name='kIOPMSettingRestartOnPowerLossKey' value='Automatic Restart On Power Loss'/>
  <string_constant name='kIOPMSettingSleepOnPowerButtonKey' value='Sleep On Power Button'/>
  <string_constant name='kIOPMSettingTimeZoneOffsetKey' value='TimeZoneOffsetSeconds'/>
  <string_constant name='kIOPMSettingWakeOnACChangeKey' value='Wake On AC Change'/>
  <string_constant name='kIOPMSettingWakeOnClamshellKey' value='Wake On Clamshell Open'/>
  <string_constant name='kIOPMSettingWakeOnRingKey' value='Wake On Modem Ring'/>
  <string_constant name='kIOPMSleepWakeUUIDKey' value='SleepWakeUUID'/>
  <string_constant name='kIOPMThermalLevelWarningKey' value='Thermal_Level_Warning'/>
  <string_constant name='kIOPMThermalWarningNotificationKey' value='com.apple.system.power.thermal_warning'/>
  <string_constant name='kIOREMSleepEnabledKey' value='REMSleepEnabled'/>
  <string_constant name='kIOSystemLoadAdvisoryBatteryLevelKey' nsstring='true' value='BatteryLevel'/>
  <string_constant name='kIOSystemLoadAdvisoryCombinedLevelKey' nsstring='true' value='CombinedLevel'/>
  <string_constant name='kIOSystemLoadAdvisoryNotifyName' value='com.apple.system.powermanagement.SystemLoadAdvisory'/>
  <string_constant name='kIOSystemLoadAdvisoryThermalLevelKey' nsstring='true' value='ThermalLevel'/>
  <string_constant name='kIOSystemLoadAdvisoryUserLevelKey' nsstring='true' value='UserLevel'/>
  <enum name='IOPMAckImplied' value='0'/>
  <enum name='IOPMAuxPowerOn' value='32'/>
  <enum name='IOPMBadSpecification' value='4'/>
  <enum name='IOPMCannotRaisePower' value='6'/>
  <enum name='IOPMClockNormal' value='4'/>
  <enum name='IOPMClockRunning' value='8'/>
  <enum name='IOPMConfigRetained' value='4096'/>
  <enum name='IOPMContextRetained' value='8192'/>
  <enum name='IOPMDeviceUsable' value='32768'/>
  <enum name='IOPMHighestState' value='2'/>
  <enum name='IOPMLowestState' value='4'/>
  <enum name='IOPMMaxPerformance' value='16384'/>
  <enum name='IOPMMaxPowerStates' value='10'/>
  <enum name='IOPMNextHigherState' value='1'/>
  <enum name='IOPMNextLowerState' value='3'/>
  <enum name='IOPMNoErr' value='0'/>
  <enum name='IOPMNoSuchState' value='5'/>
  <enum name='IOPMNotAttainable' value='1'/>
  <enum name='IOPMNotPowerManaged' value='2048'/>
  <enum name='IOPMNotYetInitialized' value='8'/>
  <enum name='IOPMParameterError' value='7'/>
  <enum name='IOPMPowerOn' value='2'/>
  <enum name='IOPMSoftSleep' value='1024'/>
  <enum name='IOPMWillAckLater' value='1'/>
  <enum name='IOPM_POWER_SOURCE_REV' value='2'/>
  <enum name='kClamshellSleepBit' value='2'/>
  <enum name='kClamshellStateBit' value='1'/>
  <enum name='kIOBatteryCharge' value='2'/>
  <enum name='kIOBatteryChargerConnect' value='1'/>
  <enum name='kIOBatteryInstalled' value='4'/>
  <enum name='kIOPMACInstalled' value='1'/>
  <enum name='kIOPMACnoChargeCapability' value='64'/>
  <enum name='kIOPMAckImplied' value='0'/>
  <enum name='kIOPMAllowSleep' value='2'/>
  <enum name='kIOPMAssertionLevelOff' value='0'/>
  <enum name='kIOPMAssertionLevelOn' value='255'/>
  <enum name='kIOPMAuxPowerOn' value='32'/>
  <enum name='kIOPMBadSpecification' value='4'/>
  <enum name='kIOPMBatteryAtWarn' value='16'/>
  <enum name='kIOPMBatteryCharging' value='2'/>
  <enum name='kIOPMBatteryDepleted' value='32'/>
  <enum name='kIOPMBatteryInstalled' value='4'/>
  <enum name='kIOPMBroadcastAggressiveness' value='1'/>
  <enum name='kIOPMCannotRaisePower' value='6'/>
  <enum name='kIOPMCapabilitiesMask' value='61574'/>
  <enum name='kIOPMChildClamp' value='128'/>
  <enum name='kIOPMChildClamp2' value='512'/>
  <enum name='kIOPMClamshellClosed' value='16'/>
  <enum name='kIOPMClamshellOpened' value='1024'/>
  <enum name='kIOPMClamshellStateOnWake' value='1024'/>
  <enum name='kIOPMClockNormal' value='4'/>
  <enum name='kIOPMClockRunning' value='8'/>
  <enum name='kIOPMClosedClamshell' value='512'/>
  <enum name='kIOPMConfigRetained' value='4096'/>
  <enum name='kIOPMContextRetained' value='8192'/>
  <enum name='kIOPMDWOverTemp' value='2048'/>
  <enum name='kIOPMDeviceUsable' value='32768'/>
  <enum name='kIOPMDisableClamshell' value='64'/>
  <enum name='kIOPMDoze' value='1024'/>
  <enum name='kIOPMDriverAssertionBluetoothHIDDevicePairedBit' value='8'/>
  <enum name='kIOPMDriverAssertionCPUBit' value='1'/>
  <enum name='kIOPMDriverAssertionExternalMediaMountedBit' value='16'/>
  <enum name='kIOPMDriverAssertionMagicPacketWakeEnabledBit' value='256'/>
  <enum name='kIOPMDriverAssertionNetworkKeepAliveActiveBit' value='512'/>
  <enum name='kIOPMDriverAssertionPreventDisplaySleepBit' value='64'/>
  <enum name='kIOPMDriverAssertionReservedBit5' value='32'/>
  <enum name='kIOPMDriverAssertionReservedBit7' value='128'/>
  <enum name='kIOPMDriverAssertionUSBExternalDeviceBit' value='4'/>
  <enum name='kIOPMEnableClamshell' value='128'/>
  <enum name='kIOPMExternalPower' value='2'/>
  <enum name='kIOPMFairValue' value='2'/>
  <enum name='kIOPMForceLowSpeed' value='256'/>
  <enum name='kIOPMGoodValue' value='3'/>
  <enum name='kIOPMHighestState' value='2'/>
  <enum name='kIOPMInitialDeviceState' value='256'/>
  <enum name='kIOPMInternalPower' value='1'/>
  <enum name='kIOPMLowPower' value='65536'/>
  <enum name='kIOPMLowestState' value='4'/>
  <enum name='kIOPMMaxPerformance' value='16384'/>
  <enum name='kIOPMMaxPowerStates' value='10'/>
  <enum name='kIOPMMessageBatteryStatusHasChanged' value='3758244096'/>
  <enum name='kIOPMMessageClamshellStateChange' value='3758309632'/>
  <enum name='kIOPMMessageDarkWakeThermalEmergency' value='3758309728'/>
  <enum name='kIOPMMessageDriverAssertionsChanged' value='3758309712'/>
  <enum name='kIOPMMessageFeatureChange' value='3758309648'/>
  <enum name='kIOPMMessageInternalBatteryFullyDischarged' value='3758309664'/>
  <enum name='kIOPMMessageSleepWakeUUIDChange' value='3758309696'/>
  <enum name='kIOPMMessageSystemPowerEventOccurred' value='3758309680'/>
  <enum name='kIOPMNextHigherState' value='1'/>
  <enum name='kIOPMNextLowerState' value='3'/>
  <enum name='kIOPMNoErr' value='0'/>
  <enum name='kIOPMNoSuchState' value='5'/>
  <enum name='kIOPMNotAttainable' value='1'/>
  <enum name='kIOPMNotPowerManaged' value='2048'/>
  <enum name='kIOPMNotYetInitialized' value='8'/>
  <enum name='kIOPMNullAssertionID' value='0'/>
  <enum name='kIOPMOverTemp' value='512'/>
  <enum name='kIOPMPSLocationLeft' value='1001'/>
  <enum name='kIOPMPSLocationRight' value='1002'/>
  <enum name='kIOPMParameterError' value='7'/>
  <enum name='kIOPMPassThrough' value='256'/>
  <enum name='kIOPMPoorValue' value='1'/>
  <enum name='kIOPMPowerButton' value='8'/>
  <enum name='kIOPMPowerEmergency' value='32'/>
  <enum name='kIOPMPowerOn' value='2'/>
  <enum name='kIOPMPreventIdleSleep' value='64'/>
  <enum name='kIOPMPreventSleep' value='4'/>
  <enum name='kIOPMPreventSystemSleep' value='16'/>
  <enum name='kIOPMProcessorSpeedChange' value='256'/>
  <enum name='kIOPMRawLowBattery' value='128'/>
  <enum name='kIOPMRestart' value='128'/>
  <enum name='kIOPMRestartCapability' value='128'/>
  <enum name='kIOPMRootDomainState' value='512'/>
  <enum name='kIOPMSleep' value='1'/>
  <enum name='kIOPMSleepCapability' value='4'/>
  <enum name='kIOPMSleepNow' value='1'/>
  <enum name='kIOPMSoftSleep' value='1024'/>
  <enum name='kIOPMStaticPowerValid' value='2048'/>
  <enum name='kIOPMSystemCapabilityAudio' value='4'/>
  <enum name='kIOPMSystemCapabilityCPU' value='1'/>
  <enum name='kIOPMSystemCapabilityDidChange' value='2'/>
  <enum name='kIOPMSystemCapabilityGraphics' value='2'/>
  <enum name='kIOPMSystemCapabilityNetwork' value='8'/>
  <enum name='kIOPMSystemCapabilityWillChange' value='1'/>
  <enum name='kIOPMThermalLevelCritical' value='10'/>
  <enum name='kIOPMThermalLevelDanger' value='5'/>
  <enum name='kIOPMThermalLevelNormal' value='0'/>
  <enum name='kIOPMThermalLevelTrap' value='110'/>
  <enum name='kIOPMThermalLevelUnknown' value='255'/>
  <enum name='kIOPMThermalLevelWarning' value='100'/>
  <enum name='kIOPMThermalWarningLevelCrisis' value='10'/>
  <enum name='kIOPMThermalWarningLevelDanger' value='100'/>
  <enum name='kIOPMThermalWarningLevelNormal' value='0'/>
  <enum name='kIOPMUMessageLegacyAutoPower' value='3758244368'/>
  <enum name='kIOPMUMessageLegacyAutoWake' value='3758244352'/>
  <enum name='kIOPMUPSInstalled' value='8'/>
  <enum name='kIOPMUndefinedValue' value='0'/>
  <enum name='kIOPMUnidleDevice' value='2'/>
  <enum name='kIOPMUnknown' value='65535'/>
  <enum name='kIOPMUserActiveLocal' value='0'/>
  <enum name='kIOPMUserActiveRemote' value='1'/>
  <enum name='kIOPMWillAckLater' value='1'/>
  <enum name='kIOSystemLoadAdvisoryLevelBad' value='1'/>
  <enum name='kIOSystemLoadAdvisoryLevelGreat' value='3'/>
  <enum name='kIOSystemLoadAdvisoryLevelOK' value='2'/>
  <enum name='kInflowForciblyEnabledBit' value='1'/>
  <enum name='kMaxType' value='7'/>
  <enum name='kNumPMMethods' value='16'/>
  <enum name='kPMActivityTickle' value='10'/>
  <enum name='kPMAllowPowerChange' value='3'/>
  <enum name='kPMCancelPowerChange' value='4'/>
  <enum name='kPMEthernetWakeOnLANSettings' value='4'/>
  <enum name='kPMGeneralAggressiveness' value='0'/>
  <enum name='kPMGetAggressiveness' value='1'/>
  <enum name='kPMGetSystemSleepType' value='11'/>
  <enum name='kPMLastAggressivenessType' value='8'/>
  <enum name='kPMMinutesToDim' value='1'/>
  <enum name='kPMMinutesToSleep' value='3'/>
  <enum name='kPMMinutesToSpinDown' value='2'/>
  <enum name='kPMMotionSensor' value='7'/>
  <enum name='kPMPowerSource' value='6'/>
  <enum name='kPMRestartSystem' value='6'/>
  <enum name='kPMSetAggressiveness' value='0'/>
  <enum name='kPMSetClamshellSleepState' value='12'/>
  <enum name='kPMSetDisplayPowerOn' value='15'/>
  <enum name='kPMSetMaintenanceWakeCalendar' value='8'/>
  <enum name='kPMSetProcessorSpeed' value='5'/>
  <enum name='kPMSetUserAssertionLevels' value='9'/>
  <enum name='kPMShutdownSystem' value='5'/>
  <enum name='kPMSleepSystem' value='2'/>
  <enum name='kPMSleepSystemOptions' value='7'/>
  <enum name='kPMSleepWakeDebugTrig' value='14'/>
  <enum name='kPMSleepWakeWatchdogEnable' value='13'/>
  <function name='IOAllowPowerChange'>
    <arg type='I'/>
    <arg type='l' type64='q'/>
    <retval type='i'/>
  </function>
  <function name='IOCancelPowerChange'>
    <arg type='I'/>
    <arg type='l' type64='q'/>
    <retval type='i'/>
  </function>
  <function name='IOCopySystemLoadAdvisoryDetailed'>
    <retval already_retained='true' type='^{__CFDictionary=}'/>
  </function>
  <function name='IODeregisterApp'>
    <arg type='^I'/>
    <retval type='i'/>
  </function>
  <function name='IODeregisterForSystemPower'>
    <arg type='^I'/>
    <retval type='i'/>
  </function>
  <function name='IOGetSystemLoadAdvisory'>
    <retval type='i'/>
  </function>
  <function name='IOPMAssertionCopyProperties'>
    <arg type='I'/>
    <retval already_retained='true' type='^{__CFDictionary=}'/>
  </function>
  <function name='IOPMAssertionCreate'>
    <arg type='^{__CFString=}'/>
    <arg type='I'/>
    <arg type='^I'/>
    <retval type='i'/>
  </function>
  <function name='IOPMAssertionCreateWithDescription'>
    <arg type='^{__CFString=}'/>
    <arg type='^{__CFString=}'/>
    <arg type='^{__CFString=}'/>
    <arg type='^{__CFString=}'/>
    <arg type='^{__CFString=}'/>
    <arg type='d'/>
    <arg type='^{__CFString=}'/>
    <arg type='^I'/>
    <retval type='i'/>
  </function>
  <function name='IOPMAssertionCreateWithName'>
    <arg type='^{__CFString=}'/>
    <arg type='I'/>
    <arg type='^{__CFString=}'/>
    <arg type='^I'/>
    <retval type='i'/>
  </function>
  <function name='IOPMAssertionCreateWithProperties'>
    <arg type='^{__CFDictionary=}'/>
    <arg type='^I'/>
    <retval type='i'/>
  </function>
  <function name='IOPMAssertionDeclareUserActivity'>
    <arg type='^{__CFString=}'/>
    <arg type='i'/>
    <arg type='^I'/>
    <retval type='i'/>
  </function>
  <function name='IOPMAssertionRelease'>
    <arg type='I'/>
    <retval type='i'/>
  </function>
  <function name='IOPMAssertionRetain'>
    <arg type='I'/>
  </function>
  <function name='IOPMAssertionSetProperty'>
    <arg type='I'/>
    <arg type='^{__CFString=}'/>
    <arg type='@'/>
    <retval type='i'/>
  </function>
  <function name='IOPMCancelScheduledPowerEvent'>
    <arg type='^{__CFDate=}'/>
    <arg type='^{__CFString=}'/>
    <arg type='^{__CFString=}'/>
    <retval type='i'/>
  </function>
  <function name='IOPMCopyAssertionsByProcess'>
    <arg type='^^{__CFDictionary}'/>
    <retval type='i'/>
  </function>
  <function name='IOPMCopyAssertionsStatus'>
    <arg type='^^{__CFDictionary}'/>
    <retval type='i'/>
  </function>
  <function name='IOPMCopyBatteryInfo'>
    <arg type='I'/>
    <arg type='^^{__CFArray}'/>
    <retval type='i'/>
  </function>
  <function name='IOPMCopyCPUPowerStatus'>
    <arg type='^^{__CFDictionary}'/>
    <retval type='i'/>
  </function>
  <function name='IOPMCopyScheduledPowerEvents'>
    <retval already_retained='true' type='^{__CFArray=}'/>
  </function>
  <function name='IOPMDeclareNetworkClientActivity'>
    <arg type='^{__CFString=}'/>
    <arg type='^I'/>
    <retval type='i'/>
  </function>
  <function name='IOPMFindPowerManagement'>
    <arg type='I'/>
    <retval type='I'/>
  </function>
  <function name='IOPMGetAggressiveness'>
    <arg type='I'/>
    <arg type='L' type64='Q'/>
    <arg type='^L' type64='^Q'/>
    <retval type='i'/>
  </function>
  <function name='IOPMGetThermalWarningLevel'>
    <arg type='^I'/>
    <retval type='i'/>
  </function>
  <function name='IOPMSchedulePowerEvent'>
    <arg type='^{__CFDate=}'/>
    <arg type='^{__CFString=}'/>
    <arg type='^{__CFString=}'/>
    <retval type='i'/>
  </function>
  <function name='IOPMSetAggressiveness'>
    <arg type='I'/>
    <arg type='L' type64='Q'/>
    <arg type='L' type64='Q'/>
    <retval type='i'/>
  </function>
  <function name='IOPMSleepEnabled'>
    <retval type='i' type64='I'/>
  </function>
  <function name='IOPMSleepSystem'>
    <arg type='I'/>
    <retval type='i'/>
  </function>
  <function name='IORegisterApp'>
    <arg type='^v'/>
    <arg type='I'/>
    <arg type='^^{IONotificationPort}'/>
    <arg function_pointer='true' type='^?'>
      <arg type='^v'/>
      <arg type='I'/>
      <arg type='I'/>
      <arg type='^v'/>
      <retval type='v'/>
    </arg>
    <arg type='^I'/>
    <retval type='I'/>
  </function>
  <function name='IORegisterForSystemPower'>
    <arg type='^v'/>
    <arg type='^^{IONotificationPort}'/>
    <arg function_pointer='true' type='^?'>
      <arg type='^v'/>
      <arg type='I'/>
      <arg type='I'/>
      <arg type='^v'/>
      <retval type='v'/>
    </arg>
    <arg type='^I'/>
    <retval type='I'/>
  </function>
</signatures>
"""

# __bundle__ = objc.initFrameworkWrapper("IOKit",
#                                        frameworkIdentifier="com.apple.framework.IOKit",
#                                        frameworkPath=objc.pathForFramework("/System/Library/Frameworks/IOKit.framework"),
#                                        globals=globals())

__bundle__ = objc.parseBridgeSupport(
    GEN_BRIDGE_METADATA,
    globals(),
    objc.pathForFramework("/System/Library/Frameworks/IOKit.framework"))

objc.loadBundleFunctions(__bundle__, globals(), [("IOPMAssertionCreateWithName", b"i@I@o^I")])
