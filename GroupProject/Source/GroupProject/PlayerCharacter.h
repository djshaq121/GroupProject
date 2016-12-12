// Copyright 

#pragma once

#include "GameFramework/Character.h"
#include "GroupProject.h"
#include "PlayerCharacter.generated.h"

//Death
DECLARE_DYNAMIC_MULTICAST_DELEGATE(FPlayerDelegate);

class AHumanPlayerController;

UCLASS()
class GROUPPROJECT_API APlayerCharacter : public ACharacter
{
	GENERATED_BODY()

		UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera", meta = (AllowPrivateAccess = "true"))
		class USpringArmComponent* SpringArm;

		UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera", meta = (AllowPrivateAccess = "true"))
		class UCameraComponent* Camera;

/*Health & Armor*/
private:
	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		int32 MaximumHealth = 100;//Its int because we dont want to compare float to zero

	UPROPERTY(VisibleAnywhere, Category = "Health & Armor")
		int32 CurrentHealth;

	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		int32 MaximumArmor = 100;//Its int because we dont want to compare float to zero

	UPROPERTY(VisibleAnywhere, Category = "Health & Armor")
		int32 CurrentArmor;

public:

	FPlayerDelegate OnDeath;

	//Make an IsDead property - So it can be caled in blueprint
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Setup")
	bool bIsDead = false;

	// Sets default values for this character's properties
	APlayerCharacter();

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;
	
	// Called every frame
	virtual void Tick( float DeltaSeconds ) override;

	virtual float TakeDamage(float DamageAmount, struct FDamageEvent const & DamageEvent, class AController * EventInstigator, AActor * DamageCauser) override;

	// Called to bind functionality to input
	virtual void SetupPlayerInputComponent(class UInputComponent* InputComponent) override;

	AHumanPlayerController* GetHumanController();

	

	void OnFire();

	UFUNCTION(BlueprintCallable, Category = "Health & Armor")
	int GetCurrentHealth() const;

	UFUNCTION(BlueprintCallable, Category = "Health & Armor")
	int GetCurrentArmor() const;

	void Heal(int Amount);

	bool GetIsDead();


/*Movement*/

public:
	void ToggleCrouch();

	UFUNCTION(BlueprintCallable, Category = "Movement")
	bool GetIsCrouching() const;

	/** Base turn rate, in deg/sec. Other scaling may affect final turn rate. */
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera")
		float BaseTurnRate;

	/** Base look up/down rate, in deg/sec. Other scaling may affect final rate. */
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera")
		float BaseLookUpRate;

	/** Called for forwards/backward input */
	void MoveForward(float Value);

	/** Called for side to side input */
	void MoveRight(float Value);

	void TurnAtRate(float Rate);

	void LookUpRate(float Rate);


private:
	
	bool bIsCrouching = false;

/*Weapon*/
public:
	void AddToInventory(class AWeaponBase* NewWeapon);

	void EquipWeapon(AWeaponBase * WeaponToEquip);

	void StartFire();
	
	void StopFire();

	void Reload();

	class AWeaponBase* Weapon;

	void SwitchToAssaultRifle();

	void SwitchToLaserLaser();


	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Setup")
	bool bIsAiming = false;

	UFUNCTION(BlueprintCallable, Category = "Aiming")
	bool GetIsAiming() const;
private:

	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		bool bEquipNewWeapon = true;
	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		FName WeaponSocketName;

	//Struct Iventory
	UPROPERTY(BlueprintReadWrite, meta = (AllowPrivateAccess = "true"), Category = Hack)
	FPlayerInventory Inventory;


protected:
	
	void CameraZoomIn();

	void CameraZoomOut();

	UPROPERTY(VisibleAnywhere, Category = "Camera")
	float CameraZoomLength;

	float CamCrouchHeight;
	FVector StartingCameraPosition;
	


};
