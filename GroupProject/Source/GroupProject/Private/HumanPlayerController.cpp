// Copyright 

#include "GroupProject.h"
#include "HumanPlayerController.h"
#include "PlayerCharacter.h"


void  AHumanPlayerController::SetPawn(APawn* InPawn)
{
	Super::SetPawn(InPawn);
	if (InPawn)//Check is the player is there
	{
		auto PossessedPlayer = Cast<APlayerCharacter>(InPawn);
		if (!ensure(PossessedPlayer)) { return; }

		//Subscribe our local methods to the players deaths
		PossessedPlayer->OnDeath.AddUniqueDynamic(this, &AHumanPlayerController::OnPossesPlayerDeath);
	}
}

void AHumanPlayerController::OnPossesPlayerDeath()
{
	StartSpectatingOnly();//When the player dies go into spectating mode 
}

void AHumanPlayerController::BeginPlay()
{
	Super::BeginPlay();

	//Finding the player and checking if the controller is possing the player
	auto ControlledPlayer = GetPawn();
	if (!ControlledPlayer)
	{
		UE_LOG(LogTemp, Warning, TEXT("Not possing player"))
	}
	else
	{
		UE_LOG(LogTemp, Warning, TEXT("Possing player"))
	}
}


void AHumanPlayerController::Tick(float DeltaSeconds)
{
}

APlayerCharacter* AHumanPlayerController::GetControlledPlayer() const
{
	return Cast<APlayerCharacter>(GetPawn());
}

void AHumanPlayerController::AimTowardsCrosshair()
{
	FVector HitLocation;//Out parameter
	if (GetSightRayHitLocation(HitLocation))
	{
		UE_LOG(LogTemp, Warning, TEXT("Hit Direction: %s "), *HitLocation.ToString());
	}
}

bool AHumanPlayerController:: GetSightRayHitLocation(FVector &HitLocation) const
{
	//Find the crosshair position in pixel coordinate
	
	int32 ViewportSizeX, ViewportSizeY;
	
	//Gets the size of the view port
	GetViewportSize(ViewportSizeX, ViewportSizeY);
	auto ScreenLocation = FVector2D(ViewportSizeX *  CrossHairXLocation, ViewportSizeY *  CrossHairYLocation);


	
	FVector LookDirection;// Out Parameter
	//De-Project the screen position of the crosshair to a world direction
	if (GetLookDirection(ScreenLocation, LookDirection))
		{
			//Line trace along the look direction 
			GetLookVectorHitLocation(LookDirection, HitLocation);
		}

	return true;
}

bool AHumanPlayerController::GetLookVectorHitLocation(FVector LookDirection, FVector & HitLocation) const
{
	
	if (GetControlledPlayer() == nullptr) { HitLocation = FVector(0); return false; }

	FHitResult HitResult;
	
	auto StartLocation = PlayerCameraManager->GetCameraLocation();//The start location of the line trace 
	auto EndLocation = StartLocation + (LookDirection * LineTraceRange); //The end location of the line trace

	if (GetWorld()->LineTraceSingleByChannel(HitResult, StartLocation, EndLocation, ECC_Visibility))
	{
		HitLocation = HitResult.Location;
		
		
		// Once we done the first line trace we return the impact point
		//The Second line trace starts from the character and the the endlocation is the impact point of the first line trace 
		auto Start = GetControlledPlayer()->GetMesh()->GetSocketLocation("WeaponSocket");
		GetWorld()->LineTraceSingleByChannel(HitResult, Start, HitLocation, ECC_Visibility);
		DrawDebugLine(GetWorld(), Start, HitLocation, FColor(0, 0, 255), true);
		return true;
	}

	HitLocation = FVector(0);
	return false;
}

bool AHumanPlayerController::GetLookDirection(FVector2D ScreenLocation, FVector & LookDirection) const
{
	FVector CameraWorldLocation;//REMOVE LATER

	//Convert current mouse 2D position to World Space 3D position and direction. Returns false if unable to determine value.
	return DeprojectScreenPositionToWorld(ScreenLocation.X, ScreenLocation.Y, CameraWorldLocation, LookDirection);
	
}

