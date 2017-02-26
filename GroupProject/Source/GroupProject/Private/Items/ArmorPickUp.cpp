// Copyright 

#include "GroupProject.h"
#include "ArmorPickUp.h"
#include "PlayerCharacter.h"

AArmorPickUp::AArmorPickUp()
{
}

void AArmorPickUp::OnPlayerEnterPickupBox(UPrimitiveComponent * OverlappedComp, AActor * OtherActor, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFomSweep, const FHitResult & SweepResult)
{

	APlayerCharacter* Player = Cast<APlayerCharacter>(OtherActor);
	if (Player)
	{
		if (Player->GetCurrentArmor() < Player->GetMaxArmor())
		{
			Player->HealArmor(ArmorAmount);
			Destroy();
		}

	}
}