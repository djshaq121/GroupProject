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

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = Default)
		FName WeaponName;

	UFUNCTION(BlueprintCallable, Category = "Default")
		FName GetWeaponName() const;

	// Sets default values for this actor's properties
	AWeaponBase();

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	// Called every frame
	virtual void Tick(float DeltaSeconds) override;

	UFUNCTION(BlueprintCallable, Category = "Weapon")
	APlayerCharacter * GetPawnOwner() const;
	UFUNCTION(BlueprintCallable, Category = "Weapon")
	void ChangeOwner(AActor* NewOwner);
	
	UFUNCTION()//Actor is gonna be us - We need to type check it so only the player can pick it up
	virtual void OnPlayerEnterPickupBox(UPrimitiveComponent* OverlappedComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFomSweep, const FHitResult& SweepResult);

	void DealDamage(const FHitResult& Hit);

	virtual void DoFire();

	void StartFire();

	void StopFire();

	virtual void OnInteract(AActor* Caller) ;
	
	void SetCanInteract(bool NewInteract);
	
	/*Weapon*/

	
	UFUNCTION(BlueprintCallable, Category = "Ammo")
	int32 GetCurrentAmmoInClip() const;

	UFUNCTION(BlueprintCallable, Category = "Ammo")
	int32 GetCurrentAmmoInGun() const;

	FVector CalcSpread() const;
	
	void Recoil();

	void Reload();

	void UseAmmo();

protected:
	UPROPERTY(EditDefaultsOnly)
	float WeaponRange = 5000;

private:
	/*Firerate timer handle*/
	FTimerHandle FireRateHandle;

	/*The Maxium amount of ammo allowed in the gun*/
	UPROPERTY(EditDefaultsOnly)
		int32 MaxAmmoInGun = 500;

	/*The Starting ammo in the clip*/
	UPROPERTY(EditDefaultsOnly)
	int32 MaxAmmoPerClip = 60;//This is the starting clip	

	
	int32 CurrentAmmoInClip;

	/*The current amount of bullets in the gun can have*/
	int32 CurrentAmmoInGun;

	/*The Base damage of the weapon*/
	UPROPERTY(EditDefaultsOnly)
		float BaseDamage;

	/*The accuracy of the gun. Where 0 has no weapon spread*/
	UPROPERTY(EditDefaultsOnly)
	float WeaponSpread = 0;
	
	UPROPERTY(EditDefaultsOnly)
	float FireRate = 0;

	/*The amount of recoil. Postivte number moves the gun right, negative left*/
	UPROPERTY(EditDefaultsOnly)
	float HorizontalRecoilAmount = 0.03f;

	/*The recoil amount. Leave as a positive number*/
	UPROPERTY(EditDefaultsOnly)
	float VerticalRecoilAmount = 0.05f;

	
	float CrossHairXLocation = 0.5;
	float CrossHairYLocation = 0.5;
	FCollisionQueryParams TraceParams;


   /*FX*/
public:

	void SpawnMuzzleEffect();
	
	void SpawnTrailEffect(FVector& EndPoint);

	void SpawnImpactEffect(FHitResult& Hit);
	

private:

	/*Muzzle Effects*/
	UPROPERTY(EditDefaultsOnly)
		UParticleSystem* ShotEffect;
	/*Bullet Trail Effects*/
	UPROPERTY(EditDefaultsOnly)
		UParticleSystem* TrailEffect;
	/*Impact Effects*/
	UPROPERTY(EditDefaultsOnly)
		UParticleSystem* ImpactEffect;

	UPROPERTY(EditDefaultsOnly)
	USoundCue* FireSound;

	UPROPERTY(EditDefaultsOnly)
	USoundCue* ImpactSound;


	int32 BSCount;
	
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

	bool bCanFire = true;

	UPROPERTY(EditDefaultsOnly, Category = "Camera")
	TSubclassOf<UCameraShake> WeaponFireShake;

private:

	

	UPROPERTY(EditDefaultsOnly)
	bool bCanInteract = true;

	bool GetLookVectorHitLocation(FVector LookDirection, FHitResult& HitResult) const;

	bool GetLookDirection(FVector2D ScreenLocation, FVector& LookDirection) const;



	/************************************************************************/
	/* Ammo & Reloading                                                     */
	/************************************************************************/

private:

	FTimerHandle TimerHandle_ReloadWeapon;

	FTimerHandle TimerHandle_StopReload;

protected:

	/* Time to assign on reload when no animation is found */
	UPROPERTY(EditDefaultsOnly, Category = "Animation")
		float NoAnimReloadDuration;

	/*UPROPERTY(Transient)
		bool bPendingReload;*/

	UPROPERTY(EditDefaultsOnly, Category = "Sounds")
		USoundCue* ReloadSound;

	UPROPERTY(EditDefaultsOnly, Category = "Animation")
		UAnimMontage* ReloadAnim;

	bool bCanReload = true;

	UAudioComponent* PlayWeaponSound(USoundCue* SoundToPlay);

	float PlayWeaponAnimation(UAnimMontage* Animation, float InPlayRate = 1.f, FName StartSectionName = NAME_None);

	void StopWeaponAnimation(UAnimMontage* Animation);
public:

		void CheckIfPlayerCanReload();

		bool GetCanReload();

		virtual void StartReload();

		virtual void StopSimulateReload();

		virtual void ReloadWeapon();
};