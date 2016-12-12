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

	UFUNCTION(BlueprintCallable, Category = "Weapon")
	APlayerCharacter * GetPawnOwner() const;
	
	// Called every frame
	virtual void Tick(float DeltaSeconds) override;

	void Reload();

	void DealDamage(const FHitResult& Hit);
	virtual void DoFire();
	void StartFire();
	void StopFire();


	UFUNCTION(BlueprintCallable, Category = "Weapon")
	void ChangeOwner(AActor* NewOwner);

	
	virtual void OnInteract(AActor* Caller) ;
	
	UFUNCTION()//Actor is gonna be us - We need to type check it so only the player can pick it up
		virtual void OnPlayerEnterPickupBox(UPrimitiveComponent* OverlappedComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFomSweep, const FHitResult& SweepResult);

	void SetCanInteract(bool NewInteract);

	UFUNCTION(BlueprintCallable, Category = "Ammo")
		int32 GetCurrentAmmoInClip() const;

	UFUNCTION(BlueprintCallable, Category = "Ammo")
		int32 GetCurrentAmmoInGun() const;

	void UseAmmo();

	void FireEffect();

	
protected:
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, meta = (AllowPirvateAccess = "true"))
		USphereComponent* CollisonSphere;
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, meta = (AllowPirvateAccess = "true"))
		USkeletalMeshComponent* WeaponMesh;
	class APlayerCharacter* OwningPlayer;
	UPROPERTY(EditDefaultsOnly)
		FName MuzzleSocketName;

	bool bIsFiring = true; //Check if the player is firing

	bool GetSightRayHitLocation(FHitResult& HitResult) const;

	//nEEDS TO MOVE INTO
	

	bool bCanFire = true;
private:

	UPROPERTY(EditDefaultsOnly)
	UParticleSystem* ShotEffect;

	UPROPERTY(EditDefaultsOnly)
	bool bCanInteract = true;

	bool GetLookVectorHitLocation(FVector LookDirection, FHitResult& HitResult) const;

	bool GetLookDirection(FVector2D ScreenLocation, FVector& LookDirection) const;

	FTimerHandle FireRateHandle;

	/*Weapon ammo on spawn*/
	//Need starting max ammo in clip 
	
	UPROPERTY(EditDefaultsOnly)
		int32 MaxAmmoInGun = 500;
	UPROPERTY(EditDefaultsOnly)
		int32 MaxAmmoPerClip = 60;//This is the starting clip
	//Dont need to see this 
		int32 CurrentAmmoInClip;
	/*The current amount of bullets in the gun can have*/
		int32 CurrentAmmoInGun;
	UPROPERTY(EditDefaultsOnly)
		float BaseDamage;
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
