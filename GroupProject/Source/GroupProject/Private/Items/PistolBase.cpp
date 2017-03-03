// Copyright LostGods

#include "GroupProject.h"
#include "PistolBase.h"
#include "PlayerCharacter.h"


//void APistolBase::StartFire()
//{
//	if (GetPawnOwner() != nullptr && !GetPawnOwner()->GetIsDead())//Stops the game from crashing when the player shoots and dies at the same time  
//	{
//		if (GetCurrentAmmoInClip() > 0 && bCanFire)
//		{
//			if (WeaponFireShake)//Checking if we have 
//			{
//				//This oscillates the camera 
//				GetWorld()->GetFirstPlayerController()->ClientPlayCameraShake(WeaponFireShake, 1.f);
//			}
//			Noise(1.f);
//			Recoil();
//			bIsFiring = true;
//			DoFire();
//
//			float TimerDelay = FireRate > 0 ? 1 / (FireRate*0.01667) : FApp::GetDeltaTime();
//
//			auto World = GetWorld();
//			if (World) {
//				//This what makes the doFire loop when its held down
//
//				if (!FireRateHandle.IsValid())
//				{
//
//					World->GetTimerManager().SetTimer(FireRateHandle, this, &AWeaponBase::StartFire, TimerDelay, true);//This will loop the startfire because we set it to true
//
//				}
//			}
//			else {
//
//				StopFire();
//
//			}
//		}
//		//This reloads when the ammo reaches zero
//		if (GetCurrentAmmoInClip() <= 0 && GetCurrentAmmoInGun() > 0 && GetCanReload()) {
//			StopFire();
//
//			StartReload();
//		}
//	}
//}

