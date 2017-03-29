// Copyright LostGods

#include "GroupProject.h"
#include "AmmoTest.h"
#include "AutomationTest.h"
#include "AutomationCommon.h"
#include "WeaponBase.h"


IMPLEMENT_SIMPLE_AUTOMATION_TEST(AmmoTest, "AmmoTest", EAutomationTestFlags::SmokeFilter | EAutomationTestFlags::EditorContext)
bool AmmoTest::RunTest(const FString& Parameters)
{
	int32 CurrentAmmoInGun = 140;
	int32 MaxAmmoPerClip = 60;
	int32 CurrentAmmoInClip =32;
	int32 NeededAmmo = MaxAmmoPerClip - CurrentAmmoInClip;

	if (CurrentAmmoInGun >= NeededAmmo)
	{

		CurrentAmmoInClip = CurrentAmmoInClip + NeededAmmo;
		CurrentAmmoInGun = CurrentAmmoInGun - NeededAmmo;
		UE_LOG(LogTemp, Log, TEXT("Value should be "));
	}	
	UE_LOG(LogTemp, Log, TEXT("THIS FORMULA IS INCORRECT "));
	return true;
}

