// Copyright 

#include "GroupProject.h"
#include "HealthPickUp.h"
#include "PlayerCharacter.h"


AHealthPickUp::AHealthPickUp()
{

}


void AHealthPickUp::OnPlayerEnterPickupBox(UPrimitiveComponent * OverlappedComp, AActor * OtherActor, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFomSweep, const FHitResult & SweepResult)
{
	
	APlayerCharacter* Player = Cast<APlayerCharacter>(OtherActor);
	if (Player)
	{
		if (Player->GetCurrentHealth() < Player->GetMaxHealth())
		{
			Player->Heal(HealthAmount);
			Destroy();
		}
		
	}
}

