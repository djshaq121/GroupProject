// Copyright 

#include "GroupProject.h"
#include "HealthPickUp.h"
#include "PlayerCharacter.h"

AHealthPickUp::AHealthPickUp()
{

}


void AHealthPickUp::OnPlayerEnterPickupBox(UPrimitiveComponent * OverlappedComp, AActor * OtherActor, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFomSweep, const FHitResult & SweepResult)
{
	UE_LOG(LogTemp, Warning, TEXT("Overlapping derived from the health pick up"))
		APlayerCharacter* Player = Cast<APlayerCharacter>(OtherActor);
	if (Player)
	{
		Player->Heal(HealthAmount);
		Destroy();
	}
}


