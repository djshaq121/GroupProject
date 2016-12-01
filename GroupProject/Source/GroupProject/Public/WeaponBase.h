// Copyright 

#pragma once

#include "GameFramework/Actor.h"
#include "GroupProject.h"
#include "WeaponBase.generated.h"



UCLASS()
class GROUPPROJECT_API AWeaponBase : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	AWeaponBase();

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;
	
	// Called every frame
	virtual void Tick(float DeltaSeconds) override;

	void DealDamage(const FHitResult& Hit);
	void DoFire();
	void StartFire();
	void StopFire();


	UFUNCTION(BlueprintCallable, Category = "Weapon")
	void ChangeOwner(AActor* NewOwner);

	void OnInteract_Implementation(AActor* Caller) ;
	

protected:
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, meta = (AllowPirvateAccess = "true"))
		USphereComponent* CollisonSphere;
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, meta = (AllowPirvateAccess = "true"))
		USkeletalMeshComponent* WeaponMesh;
	class APlayerCharacter* OwningPlayer;
private:


	bool GetSightRayHitLocation(FHitResult& HitResult) const;

	bool GetLookVectorHitLocation(FVector LookDirection, FHitResult& HitResult) const;

	bool GetLookDirection(FVector2D ScreenLocation, FVector& LookDirection) const;

	FTimerHandle FireRateHandle;

	/*Weapon ammo on spawn*/
	UPROPERTY(EditDefaultsOnly)
		int32 StartAmmoClip = 60;
	UPROPERTY(EditDefaultsOnly)
		int32 MaxAmmo = 500;
	UPROPERTY(EditDefaultsOnly)
		int32 MaxAmmoPerClip = 60;
	UPROPERTY(EditDefaultsOnly)
		int32 CurrentAmmoInClip;
	/*The amount of total bullets the gun can have*/
	UPROPERTY(EditDefaultsOnly)
		int32 CurrentMaxAmmoInGun = 440;
	UPROPERTY(EditDefaultsOnly)
		int32 BaseDamage;
	UPROPERTY(EditDefaultsOnly)
		float LineTraceRange = 5000;
	UPROPERTY(EditDefaultsOnly)
		float FireRate = 0;
	UPROPERTY(VisibleAnywhere)
		float CrossHairXLocation = 0.5;
	UPROPERTY(VisibleAnywhere)
		float CrossHairYLocation = 0.5;
	FCollisionQueryParams TraceParams;
	
};
