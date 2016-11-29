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

	void DealDamage();
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
	/*Weapon ammo on spawn*/
	UPROPERTY(EditDefaultsOnly)
		int32 StartAmmo;
	UPROPERTY(EditDefaultsOnly)
		int32 MaxAmmo = 0;
	UPROPERTY(EditDefaultsOnly)
		int32 MaxAmmoPerClip;
	UPROPERTY(EditDefaultsOnly)
		int32 CurrentAmmoInClip;

	FCollisionQueryParams TraceParams;
	
};
